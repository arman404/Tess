require('dotenv').config();
const { Telegraf, Markup } = require('telegraf');
const nodemailer = require('nodemailer');
const fs = require('fs');
const path = require('path');

// ============================================================
//  KONFIGURASI
// ============================================================
const BOT_TOKEN = process.env.BOT_TOKEN || 'TOKEN BOT LU';
const EMAIL_USER = process.env.EMAIL_USER || 'ISI EMAIL LU YANG MAU LU PAKE';
const EMAIL_PASS = process.env.EMAIL_PASS || 'ISI APP PASSWORD EMAIL LU';
const ADMIN_ID = parseInt(process.env.ADMIN_ID) || ID LU;
const DATA_FILE = path.join(__dirname, 'data.json');

const DEFAULT_CHANNELS = [
    '@Pp3k5rlAGzFjNDI1',
    '@ybWHEGq-xSdjZGE1'
];

// ============================================================
//  DATA STORE
// ============================================================
let data = {
    users: {},
    emails: [],
    targetEmails: [],
    redeemCodes: {},
    lockedChannels: [],
    totalReports: 0,
    lastEmailIndex: 0,
    defaultEmailIndex: 0,
    requiredChannels: DEFAULT_CHANNELS
};

if (fs.existsSync(DATA_FILE)) {
    try {
        const loaded = JSON.parse(fs.readFileSync(DATA_FILE));
        data = { ...data, ...loaded };
        console.log('📂 Data loaded');
    } catch (e) {
        console.log('⚠️ Load data gagal, pakai default');
    }
}

function saveData() {
    try {
        fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
    } catch (e) {
        console.error('❌ Gagal save data:', e);
    }
}
setInterval(saveData, 30000);

if (!data.targetEmails || data.targetEmails.length === 0) {
    data.targetEmails = [
        'abuse@telegram.org',
        'support@telegram.org',
        'report@telegram.org',
        'business@telegram.org',
        'developers@telegram.org',
        'reclaim@telegram.org',
        'copyright@telegram.org',
        'complaints@telegram.org',
        'legal@telegram.org',
        'ios@telegram.org',
        'android@telegram.org',
        'desktop@telegram.org',
        'web@telegram.org',
        'api@telegram.org',
        'feedback@telegram.org',
        'spam@telegram.org',
        'scam@telegram.org',
        'moderator@telegram.org',
        'admin@telegram.org',
        'security@telegram.org',
        'login@stel.com',
        'support@stel.com',
        'abuse@stel.com',
        'support@group-ib.com',
        'response@cert-gib.com',
        'team@coinmarketcap.com',
        'report@coinmarketcap.com',
        'support@coinmarketcap.zendesk.com',
        'supportdesk@coinmarketcap.com'
    ];
    saveData();
}

// ============================================================
//  INISIALISASI BOT
// ============================================================
const bot = new Telegraf(BOT_TOKEN, {
    telegram: { timeout: 60000 }
});

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: { user: EMAIL_USER, pass: EMAIL_PASS },
    tls: { rejectUnauthorized: false }
});

const userSession = new Map();

// ============================================================
//  FUNGSI USER
// ============================================================
function getUser(userId) {
    if (!data.users[userId]) {
        data.users[userId] = {
            limit: 5,
            lastClaim: 0,
            isPremium: false,
            redeemedCodes: [],
            preferredEmail: null,
            verified: false
        };
        saveData();
    }
    return data.users[userId];
}

function getLimit(userId) {
    if (userId === ADMIN_ID) return Infinity;
    return getUser(userId).limit;
}

function deductLimit(userId) {
    if (userId === ADMIN_ID) return true;
    const user = getUser(userId);
    if (user.limit <= 0) return false;
    user.limit--;
    saveData();
    return true;
}

function addLimit(userId, amount) {
    if (userId === ADMIN_ID) return;
    const user = getUser(userId);
    user.limit += amount;
    saveData();
}

function canClaimDaily(userId) {
    if (userId === ADMIN_ID) return true;
    const user = getUser(userId);
    return (Date.now() - user.lastClaim) >= 24 * 60 * 60 * 1000;
}

function claimDaily(userId) {
    if (userId === ADMIN_ID) return;
    const user = getUser(userId);
    user.lastClaim = Date.now();
    user.limit += 8;
    saveData();
}

function redeemCode(userId, code) {
    code = code.toUpperCase();
    if (!data.redeemCodes[code] || data.redeemCodes[code].used) {
        return { success: false, message: '❌ Kode tidak valid atau sudah dipakai.' };
    }
    const user = getUser(userId);
    if (user.redeemedCodes.includes(code)) {
        return { success: false, message: '❌ Anda sudah pernah memakai kode ini.' };
    }
    user.limit += 5;
    user.redeemedCodes.push(code);
    data.redeemCodes[code].used = true;
    saveData();
    return { success: true, message: `✅ +5 limit! Sisa: ${user.limit}` };
}

function createRedeemCode(code) {
    code = code.toUpperCase();
    if (data.redeemCodes[code]) return { success: false, message: '❌ Kode sudah ada.' };
    data.redeemCodes[code] = { used: false };
    saveData();
    return { success: true, message: `✅ Kode ${code} dibuat.` };
}

function deleteRedeemCode(code) {
    code = code.toUpperCase();
    if (!data.redeemCodes[code]) return { success: false, message: '❌ Kode tidak ditemukan.' };
    delete data.redeemCodes[code];
    saveData();
    return { success: true, message: `✅ Kode ${code} dihapus.` };
}

// ============================================================
//  VERIFIKASI CHANNEL
// ============================================================
async function checkUserVerification(ctx, userId, forceCheck = true) {
    if (userId === ADMIN_ID) return true;
    const user = getUser(userId);
    if (!forceCheck && user.verified) return true;

    let allJoined = true;
    const failedChannels = [];
    const invalidChannels = [];

    for (const ch of data.requiredChannels) {
        if (ch.startsWith('+')) {
            console.log(`⚠️ Channel ${ch} adalah invite link, tidak bisa dicek`);
            invalidChannels.push(ch);
            continue;
        }

        const chatId = ch.replace('@', '');
        try {
            const chatMember = await ctx.telegram.getChatMember(chatId, userId);
            const status = chatMember.status;
            if (!['member', 'administrator', 'creator'].includes(status)) {
                allJoined = false;
                failedChannels.push(ch);
                console.log(`❌ User ${userId} belum join ${ch} (status: ${status})`);
            } else {
                console.log(`✅ User ${userId} sudah join ${ch}`);
            }
        } catch (err) {
            console.log(`⚠️ Gagal cek user di ${ch}: ${err.message}`);
            if (err.message.includes('400') || err.message.includes('Chat not found')) {
                invalidChannels.push(ch);
                console.log(`❌ Channel ${ch} tidak valid (link invite atau private)`);
            } else {
                allJoined = false;
                failedChannels.push(ch);
            }
        }
    }

    if (invalidChannels.length > 0) {
        const msg = `⚠️ *Channel tidak valid (harus username publik @):*\n${invalidChannels.map(ch => `- ${ch}`).join('\n')}\n\nGunakan /setchannel untuk perbaiki.`;
        await ctx.telegram.sendMessage(ADMIN_ID, msg).catch(() => {});
    }

    if (invalidChannels.length > 0 && failedChannels.length === 0) {
        allJoined = true;
    }

    if (allJoined) {
        if (!user.verified) {
            user.verified = true;
            saveData();
            console.log(`✅ User ${userId} terverifikasi`);
        }
    } else {
        if (user.verified) {
            user.verified = false;
            saveData();
            console.log(`🔄 Verifikasi user ${userId} dibatalkan (belum join: ${failedChannels.join(', ')})`);
        }
    }
    return allJoined;
}

function getVerificationKeyboard(userId) {
    if (userId) {
        const user = getUser(userId);
        if (user.verified) {
            return mainMenu(user.isPremium);
        }
    }
    const joinButtons = data.requiredChannels
        .filter(ch => !ch.startsWith('+'))
        .map(ch => {
            const link = `https://t.me/${ch.replace('@', '')}`;
            return Markup.button.url(`📢 Join ${ch}`, link);
        });
    const rows = [];
    for (let i = 0; i < joinButtons.length; i += 2) {
        rows.push(joinButtons.slice(i, i + 2));
    }
    const hasInvalid = data.requiredChannels.some(ch => ch.startsWith('+'));
    if (hasInvalid) {
        rows.push([Markup.button.callback('⚠️ Ada channel tidak valid', 'invalid_channel')]);
    }
    rows.push([
        Markup.button.callback('🔄 Cek & Verifikasi', 'verify'),
        Markup.button.callback('❓ Bantuan Verifikasi', 'help_verify')
    ]);
    return Markup.inlineKeyboard(rows);
}

// ============================================================
//  MIDDLEWARE VERIFIKASI
// ============================================================
async function ensureVerified(ctx, next) {
    const userId = ctx.from.id;
    if (userId === ADMIN_ID) return next();
    const user = getUser(userId);
    if (user.verified) return next();

    const verified = await checkUserVerification(ctx, userId, true);
    if (verified) return next();

    const msg = `
🚫 *AKSES DIBLOKIR!*  
Untuk menggunakan layanan bot ini, Anda wajib bergabung ke channel-channel di bawah ini:

${data.requiredChannels.filter(ch => !ch.startsWith('+')).map(ch => `Join ${ch}`).join('\n')}
${data.requiredChannels.some(ch => ch.startsWith('+')) ? '\n⚠️ Ada channel tidak valid, hubungi admin.' : ''}
    `;
    await ctx.replyWithMarkdown(msg, getVerificationKeyboard(userId));
    return;
}

// ============================================================
//  EMAIL SERVICE
// ============================================================
const emailSessions = {};

function createTransporter(user, pass) {
    if (!user || !pass) throw new Error('❌ Credentials tidak lengkap.');
    return nodemailer.createTransport({
        service: 'gmail',
        auth: { user, pass },
        tls: { rejectUnauthorized: false }
    });
}

async function testAndCreateSession(email, password) {
    try {
        const transporter = createTransporter(email, password);
        await transporter.verify();
        emailSessions[email] = transporter;
        return { success: true, message: '✅ Session berhasil.' };
    } catch (err) {
        return { success: false, message: `❌ Gagal session: ${err.message.substring(0, 60)}...` };
    }
}

async function sendEmailWithFallback(email, pass, target, subject, content) {
    try {
        let transporter = emailSessions[email];
        if (!transporter) {
            const result = await testAndCreateSession(email, pass);
            if (!result.success) return { success: false, message: '❌ Gagal buat session' };
            transporter = emailSessions[email];
        }
        const sendPromise = transporter.sendMail({
            from: `"Scam Reporter" <${email}>`,
            to: target,
            subject,
            text: content
        });
        const timeoutPromise = new Promise((_, reject) =>
            setTimeout(() => reject(new Error('Timeout 30s')), 30000)
        );
        await Promise.race([sendPromise, timeoutPromise]);
        return { success: true, message: '✅' };
    } catch (err) {
        console.log(`❌ Gagal kirim ke ${target} dengan ${email}: ${err.message}`);
        // Coba refresh session jika error limit/auth
        if (err.message && (err.message.includes('limit') || err.message.includes('auth') || err.message.includes('login'))) {
            const result = await testAndCreateSession(email, pass);
            if (result.success) {
                try {
                    const sendPromise = emailSessions[email].sendMail({
                        from: `"Scam Reporter" <${email}>`,
                        to: target,
                        subject,
                        text: content
                    });
                    const timeoutPromise = new Promise((_, reject) =>
                        setTimeout(() => reject(new Error('Timeout 30s')), 30000)
                    );
                    await Promise.race([sendPromise, timeoutPromise]);
                    return { success: true, message: '✅' };
                } catch (e) {
                    console.log(`❌ Gagal kirim ulang: ${e.message}`);
                    return { success: false, message: '❌ Gagal kirim ulang' };
                }
            }
        }
        return { success: false, message: '❌ Gagal kirim' };
    }
}

// ============================================================
//  GENERATE EMAIL CONTENT
// ============================================================
function generateEmailContent(data) {
    const now = new Date().toLocaleString('id-ID', {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
    const tag = data.type === 'channel' ? ' 🏷️ SCAM CHANNEL' : '';
    return `
========================================
LAPORAN SCAM TELEGRAM${tag}
========================================
Tanggal     : ${now}
Pelapor     : ${data.reporter || 'Anonymous'}
Username    : ${data.username || 'Tidak diketahui'}
Tipe Scam   : ${data.type || 'Tidak diketahui'}
Deskripsi   :
${data.description || 'Tidak ada deskripsi'}
========================================
    `;
}

// ============================================================
//  KIRIM LAPORAN (satu kali, tanpa loop)
// ============================================================
async function sendReportToAllTargets(userId, username, scamType, description, reporter) {
    const now = new Date().toLocaleString('id-ID');
    const content = `
========================================
LAPORAN SCAM TELEGRAM
========================================
Tanggal     : ${now}
Pelapor     : ${reporter}
Username    : ${username}
Tipe Scam   : ${scamType}
Deskripsi   :
${description}
========================================
    `;

    if (!data.emails || data.emails.length === 0) {
        return { success: false, message: '❌ Tidak ada akun email.', successCount: 0, failCount: 0 };
    }
    if (!data.targetEmails || data.targetEmails.length === 0) {
        return { success: false, message: '❌ Tidak ada target email.', successCount: 0, failCount: 0 };
    }

    const user = getUser(userId);
    let selectedIndex = null;
    if (user.isPremium && user.preferredEmail !== null && user.preferredEmail !== undefined) {
        if (user.preferredEmail >= 0 && user.preferredEmail < data.emails.length) {
            selectedIndex = user.preferredEmail;
        }
    }
    let emailIndex;
    if (selectedIndex !== null) {
        emailIndex = selectedIndex;
    } else if (data.defaultEmailIndex >= 0 && data.defaultEmailIndex < data.emails.length) {
        emailIndex = data.defaultEmailIndex;
    } else {
        if (typeof data.lastEmailIndex !== 'number' || isNaN(data.lastEmailIndex) || data.lastEmailIndex >= data.emails.length) {
            data.lastEmailIndex = 0;
        }
        emailIndex = data.lastEmailIndex;
    }

    const acc = data.emails[emailIndex];
    if (!acc) return { success: false, message: '❌ Akun email tidak valid.', successCount: 0, failCount: 0 };

    let successCount = 0, failCount = 0;
    for (const target of data.targetEmails) {
        const result = await sendEmailWithFallback(
            acc.user, acc.pass,
            target,
            `[SCAM REPORT] ${username}`,
            content
        );
        if (result.success) {
            successCount++;
        } else {
            failCount++;
        }
        await new Promise(resolve => setTimeout(resolve, 500)); // kurangi delay
    }

    if (selectedIndex === null) {
        data.lastEmailIndex = (emailIndex + 1) % data.emails.length;
        saveData();
    }

    return {
        success: true,
        message: `✅ ${successCount} berhasil, ❌ ${failCount} gagal (via ${acc.user})`,
        successCount,
        failCount
    };
}

// ============================================================
//  FUNGSI KIRIM LAPORAN DENGAN LOOP & DELAY
// ============================================================
async function sendReportLoop(userId, sessionData) {
    const { username, type, description, reporter, loopCount, delaySeconds } = sessionData;
    const totalLoop = loopCount || 1;
    const delayMs = (delaySeconds || 5) * 1000;

    let overallSuccess = 0;
    let overallFail = 0;
    const allResults = [];

    for (let i = 0; i < totalLoop; i++) {
        const result = await sendReportToAllTargets(userId, username, type, description, reporter);
        if (result.success) {
            overallSuccess += result.successCount;
            overallFail += result.failCount;
            allResults.push({
                loop: i + 1,
                successCount: result.successCount,
                failCount: result.failCount,
                message: `✅ ${result.successCount} berhasil, ❌ ${result.failCount} gagal`
            });
        } else {
            overallFail += 1;
            allResults.push({
                loop: i + 1,
                successCount: 0,
                failCount: 1,
                message: `❌ Gagal total: ${result.message}`
            });
        }
        if (i < totalLoop - 1 && delayMs > 0) {
            await new Promise(resolve => setTimeout(resolve, delayMs));
        }
    }

    return {
        success: true,
        totalLoop,
        overallSuccess,
        overallFail,
        allResults,
        summary: `✅ Total berhasil: ${overallSuccess} email, ❌ Total gagal: ${overallFail} email dari ${totalLoop} kali pengiriman.`
    };
}

// ============================================================
//  TAG SCAM (dengan pilihan email untuk premium)
// ============================================================
async function sendTagScamEmail(userId, channel, reporter) {
    const user = getUser(userId);
    let emailIndex = null;
    if (user.isPremium && user.preferredEmail !== null && user.preferredEmail !== undefined) {
        if (user.preferredEmail >= 0 && user.preferredEmail < data.emails.length) {
            emailIndex = user.preferredEmail;
        }
    }
    if (emailIndex === null) {
        emailIndex = (data.defaultEmailIndex >= 0 && data.defaultEmailIndex < data.emails.length) ? data.defaultEmailIndex : 0;
    }
    const acc = data.emails[emailIndex];
    if (!acc) return { success: false, message: '❌ Akun email tidak ditemukan.' };

    const now = new Date().toLocaleString('id-ID');
    const content = `
========================================
🏷️ TAG SCAM CHANNEL
========================================
Channel     : ${channel}
Pelapor     : ${reporter}
Tanggal     : ${now}

⚠️ PERINGATAN: Channel ini terbukti scam!  
Laporkan segera! #GrenXHarimau #AntiScam
========================================
    `;

    try {
        const transporter = createTransporter(acc.user, acc.pass);
        for (const target of data.targetEmails) {
            await transporter.sendMail({
                from: `"Scam Reporter" <${acc.user}>`,
                to: target,
                subject: `[TAG SCAM] ${channel}`,
                text: content
            });
            await new Promise(resolve => setTimeout(resolve, 500));
        }
        return { success: true, message: `✅ Tag scam untuk ${channel} terkirim ke ${data.targetEmails.length} email via ${acc.user}` };
    } catch (err) {
        console.error(`❌ Gagal kirim tag scam: ${err.message}`);
        return { success: false, message: `❌ Gagal kirim tag scam: ${err.message}` };
    }
}

// ============================================================
//  KEYBOARD & MENU
// ============================================================
const mainMenu = Markup.inlineKeyboard([
    [Markup.button.callback('📝 Lapor Scam', 'report', { style: 'danger' })],
    [Markup.button.callback('🏷️ Tag Scam (Premium)', 'scam_tag', { style: 'primary' })],
    [Markup.button.callback('📧 Kelola Email', 'manage_emails')],
    [Markup.button.callback('ℹ️ Bantuan', 'help'), Markup.button.callback('📊 Status', 'status', { style: 'success' })],
    [Markup.button.callback('👑 Add Owner', 'addowner'), Markup.button.callback('👑 Del Owner', 'delowner', { style: 'danger' })],
    [Markup.button.callback('⭐ Premium', 'premium'), Markup.button.callback('💰 Add Credit', 'addcredit'), Markup.button.callback('🪙 Credit', 'credit', { style: 'primary' })]
]);

const confirmKeyboard = Markup.inlineKeyboard([
    [Markup.button.callback('✅ Kirim', 'confirm_yes')],
    [Markup.button.callback('❌ Batal', 'confirm_no')]
]);

const afterReportKeyboard = Markup.inlineKeyboard([
    [Markup.button.callback('📝 Lapor Lagi', 'report')],
    [Markup.button.callback('🏠 Menu', 'menu')]
]);

// ============================================================
//  COMMAND /start
// ============================================================
bot.start(async (ctx) => {
    const userId = ctx.from.id;
    const user = getUser(userId);
    const isAdmin = userId === ADMIN_ID;

    const verified = await checkUserVerification(ctx, userId, true);
    if (!verified) {
        const msg = `
🚫 *AKSES DIBLOKIR!*  
Untuk menggunakan layanan bot ini, Anda wajib bergabung ke ${data.requiredChannels.length} channel sponsor kami terlebih dahulu di bawah ini:

${data.requiredChannels.map(ch => `Join ${ch}`).join('\n')}
        `;
        return ctx.replyWithMarkdown(msg, getVerificationKeyboard(userId));
    }

    let msg = `
🤖 *MURTAG FREE VVIP BOT*
━━━━━━━━━━━━━━━━━━━━━

👤 *INFORMASI PENGGUNA:*
- ID: \`${userId}\`
- Sisa Limit: ${isAdmin ? '∞ (Admin)' : user.limit}
- Status: ${user.isPremium ? '👑 Premium' : '🆓 Gratis'}

📌 *FITUR PENGGUNA:*
/report @username ID - Lapor penipu
/claim - Klaim +8 limit/hari
/redeem kode - Tukar kode +5 limit
/status - Cek status
/help - Bantuan
`;

    if (user.isPremium) {
        const email = (user.preferredEmail !== null && data.emails[user.preferredEmail]) ? data.emails[user.preferredEmail].user : '❌ Belum (pakai default)';
        msg += `\n📧 Email pilihan: ${email}`;
        msg += `\n/setemail <index> - Pilih email favorit (atau via tombol)`;
    }

    if (isAdmin) {
        msg += `
━━━━━━━━━━━━━━━━━━━━━
🔐 *FITUR DEVELOPER:*
/addlimit ID Jumlah
/addgmail email pass
/addtargetemail email
/deltargetemail email
/setch @ch1 @ch2
/delch
/addredeem kode
/delredeem kode
/listemail
/listtarget
/setdefaultemail index
/addprem ID
/setchannel @ch1 @ch2 ... - Ubah channel wajib
/checkch - Cek status channel
`;
    }

    msg += `
━━━━━━━━━━━━━━━━━━━━━
📤 *EMAIL TUJUAN:*
${data.targetEmails.map((e, i) => `${i+1}. ${e}`).join('\n')}
`;

    ctx.replyWithMarkdown(msg, mainMenu(user.isPremium));
});

// ============================================================
//  ACTION VERIFIKASI
// ============================================================
bot.action('verify', async (ctx) => {
    const userId = ctx.from.id;
    if (userId === ADMIN_ID) {
        ctx.answerCbQuery('Admin terverifikasi');
        return ctx.reply('Anda admin, akses penuh.');
    }
    await ctx.reply('🔄 Mengecek keanggotaan...');
    const verified = await checkUserVerification(ctx, userId, true);
    if (verified) {
        ctx.answerCbQuery('✅ Verifikasi berhasil!');
        ctx.deleteMessage().catch(() => {});
        ctx.reply('✅ Verifikasi berhasil! Gunakan /start untuk mulai.');
    } else {
        ctx.answerCbQuery('❌ Belum join semua');
        let msg = '❌ Anda belum join semua channel wajib.\n\n';
        for (const ch of data.requiredChannels) {
            if (ch.startsWith('+')) continue;
            try {
                const chatMember = await ctx.telegram.getChatMember(ch.replace('@', ''), userId);
                const status = chatMember.status;
                if (!['member', 'administrator', 'creator'].includes(status)) {
                    msg += `- ${ch} (status: ${status})\n`;
                }
            } catch (err) {
                msg += `- ${ch} (gagal cek: ${err.message})\n`;
            }
        }
        msg += '\nSilakan join semua channel, lalu klik verifikasi lagi.';
        ctx.reply(msg, getVerificationKeyboard(userId));
    }
});

bot.action('help_verify', async (ctx) => {
    ctx.answerCbQuery();
    const msg = `
📖 *Cara Verifikasi:*
1. Klik tombol "Join" untuk setiap channel di atas.
2. Setelah bergabung ke *semua* channel, klik tombol "🔄 Cek & Verifikasi".
3. Jika masih gagal, pastikan bot adalah admin di channel (hubungi admin).

*Catatan:* Channel harus berupa username publik (berawalan @), bukan link invite.
`;
    ctx.replyWithMarkdown(msg);
});

bot.action('invalid_channel', async (ctx) => {
    ctx.answerCbQuery();
    const msg = `
⚠️ *Channel tidak valid!*
Channel yang digunakan harus berupa **username publik** (contoh: @infoarlend), bukan link invite.

Gunakan perintah /setchannel untuk memperbaiki daftar channel wajib.
Contoh: /setchannel @infoarlend @lelendnih @arlendajadah @informationarta @morexxzytzyy
`;
    ctx.replyWithMarkdown(msg);
});

// ============================================================
//  COMMAND /report (memulai alur)
// ============================================================
bot.command('report', ensureVerified, (ctx) => {
    const userId = ctx.from.id;
    const user = getUser(userId);
    if (userId !== ADMIN_ID && user.limit <= 0) {
        return ctx.reply('❌ Kuota habis. /claim atau /redeem.');
    }
    userSession.delete(userId);
    userSession.set(userId, {
        step: 'username',
        data: { reporter: ctx.from.username || ctx.from.first_name, loopCount: 1, delaySeconds: 5 }
    });
    ctx.reply('📱 Masukkan *username* atau ID akun scam (contoh: @scammer_bot):');
});

// ============================================================
//  COMMAND LAINNYA (claim, redeem, status, help, scam_tag, setemail)
// ============================================================
bot.command('claim', ensureVerified, async (ctx) => {
    const userId = ctx.from.id;
    if (!canClaimDaily(userId)) {
        const next = new Date(getUser(userId).lastClaim + 24*60*60*1000);
        return ctx.reply(`⏳ Sudah claim. Coba lagi ${next.toLocaleString('id-ID')}.`);
    }
    claimDaily(userId);
    ctx.replyWithMarkdown(`🎁 *+8 Limit!* 💳 Sisa: ${userId === ADMIN_ID ? '∞' : getUser(userId).limit}`);
});

bot.command('redeem', ensureVerified, async (ctx) => {
    const userId = ctx.from.id;
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /redeem <kode>');
    const result = redeemCode(userId, args[1]);
    ctx.reply(result.message);
});

bot.command('status', ensureVerified, async (ctx) => {
    const userId = ctx.from.id;
    const user = getUser(userId);
    let msg = `📊 *Status*\n🆔 ${userId}\n💳 Limit: ${userId === ADMIN_ID ? '∞' : user.limit}\n⏳ Claim: ${canClaimDaily(userId) ? '✅ Tersedia' : '⏳ Tunggu'}\n👑 Premium: ${user.isPremium ? '✅' : '❌'}`;
    if (user.isPremium && user.preferredEmail !== null && data.emails[user.preferredEmail]) {
        msg += `\n📧 Email: ${data.emails[user.preferredEmail].user}`;
    }
    if (userId === ADMIN_ID) {
        msg += `\n\n📊 *Statistik*\n📤 Total laporan: ${data.totalReports}\n📧 Email terdaftar: ${data.emails.length}\n📤 Target email: ${data.targetEmails.length}\n🔑 Redeem codes: ${Object.keys(data.redeemCodes).length}\n📢 Channel wajib: ${data.requiredChannels.join(', ')}`;
    }
    ctx.replyWithMarkdown(msg);
});

bot.help(ensureVerified, async (ctx) => {
    const userId = ctx.from.id;
    const isAdmin = userId === ADMIN_ID;
    const isPremium = getUser(userId).isPremium;
    let msg = `
📖 *BANTUAN PENGGUNA*
/report @username ID
/claim
/redeem kode
/status
`;
    if (isPremium) {
        msg += `/scam_tag (Premium)\n/setemail index (Premium)\n📧 Gunakan tombol "Ganti Email" di menu\n`;
    }
    if (isAdmin) {
        msg += `
🔐 *BANTUAN DEVELOPER*
/addlimit ID Jumlah
/addgmail email pass
/addtargetemail email
/deltargetemail email
/setch @ch1 @ch2
/delch
/addredeem kode
/delredeem kode
/listemail
/listtarget
/setdefaultemail index
/addprem ID
/setchannel @ch1 @ch2 ... - Ubah channel wajib
/checkch - Cek status channel
`;
    }
    ctx.replyWithMarkdown(msg, mainMenu(isPremium));
});

bot.command('scam_tag', ensureVerified, async (ctx) => {
    const userId = ctx.from.id;
    const user = getUser(userId);
    if (!user.isPremium) return ctx.reply('⛔ Hanya Premium.');
    if (data.emails.length === 0) return ctx.reply('❌ Belum ada email.');
    let msg = '🏷️ *Pilih email untuk tag scam:*\n\n';
    const buttons = [];
    data.emails.forEach((acc, i) => {
        const selected = (user.preferredEmail === i) ? ' ✅' : '';
        msg += `${i+1}. ${acc.user}${selected}\n`;
        buttons.push(Markup.button.callback(`${i+1}. ${acc.user}`, `select_email_${i}`));
    });
    buttons.push(Markup.button.callback('🔙 Pakai Default', 'use_default_email'));
    buttons.push(Markup.button.callback('❌ Batal', 'cancel_tag'));
    const emailKeyboard = Markup.inlineKeyboard(buttons.map(b => [b]));
    ctx.replyWithMarkdown(msg, emailKeyboard);
});

bot.command('setemail', ensureVerified, async (ctx) => {
    const userId = ctx.from.id;
    const user = getUser(userId);
    if (!user.isPremium) return ctx.reply('⛔ Hanya Premium.');
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /setemail <index>');
    const idx = parseInt(args[1]);
    if (isNaN(idx) || idx < 0 || idx >= data.emails.length) return ctx.reply(`❌ Index tidak valid. Total: ${data.emails.length}`);
    user.preferredEmail = idx;
    saveData();
    ctx.reply(`✅ Email diatur ke ${data.emails[idx].user}.`);
});

// ============================================================
//  ADMIN COMMANDS
// ============================================================
bot.command('addprem', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /addprem <user_id>');
    const id = parseInt(args[1]);
    if (isNaN(id)) return ctx.reply('❌ ID tidak valid.');
    const user = getUser(id);
    user.isPremium = true;
    saveData();
    ctx.reply(`✅ User ${id} sekarang Premium.`);
});

bot.command('setdefaultemail', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /setdefaultemail <index>');
    const idx = parseInt(args[1]);
    if (isNaN(idx) || idx < 0 || idx >= data.emails.length) return ctx.reply(`❌ Index tidak valid. Total: ${data.emails.length}`);
    data.defaultEmailIndex = idx;
    saveData();
    ctx.reply(`✅ Email default untuk semua user: ${data.emails[idx].user}`);
});

bot.command('setchannel', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /setchannel @ch1 @ch2 ...');
    const channels = args.slice(1);
    const invalid = channels.filter(ch => !ch.startsWith('@'));
    if (invalid.length > 0) {
        return ctx.reply(`❌ Channel tidak valid (harus diawali @):\n${invalid.join('\n')}`);
    }
    data.requiredChannels = channels;
    for (const uid in data.users) {
        data.users[uid].verified = false;
    }
    saveData();
    ctx.reply(`✅ Channel wajib diupdate:\n${data.requiredChannels.join('\n')}\n⚠️ Semua user harus verifikasi ulang.`);
});

bot.command('checkch', async (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    let msg = '📢 *Status Channel Wajib:*\n\n';
    for (const ch of data.requiredChannels) {
        if (ch.startsWith('+')) {
            msg += `${ch} : ⚠️ Invite link (tidak valid)\n`;
            continue;
        }
        const chatId = ch.replace('@', '');
        try {
            const botMember = await ctx.telegram.getChatMember(chatId, ctx.botInfo.id);
            const status = botMember.status;
            msg += `${ch} : Bot adalah *${status}*\n`;
        } catch (err) {
            msg += `${ch} : ❌ Gagal akses (${err.message})\n`;
        }
    }
    ctx.replyWithMarkdown(msg);
});

bot.command('addlimit', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 3) return ctx.reply('❌ /addlimit ID Jumlah');
    const id = parseInt(args[1]);
    const amount = parseInt(args[2]);
    if (isNaN(id) || isNaN(amount)) return ctx.reply('❌ ID atau jumlah tidak valid.');
    addLimit(id, amount);
    ctx.reply(`✅ Limit user ${id} +${amount}. Sisa: ${id === ADMIN_ID ? '∞' : getUser(id).limit}`);
});

bot.command('addgmail', async (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 3) return ctx.reply('❌ /addgmail email pass');
    const email = args[1];
    const pass = args.slice(2).join(' ');
    if (data.emails.some(e => e.user === email)) return ctx.reply('❌ Email sudah terdaftar.');
    await ctx.reply(`⏳ Verifikasi ${email}...`);
    const result = await testAndCreateSession(email, pass);
    if (result.success) {
        data.emails.push({ user: email, pass });
        saveData();
        ctx.reply(`✅ ${email} berhasil ditambahkan.`);
    } else {
        ctx.reply(`❌ Gagal: ${result.message}`);
    }
});

bot.command('addtargetemail', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /addtargetemail email');
    const email = args[1];
    if (data.targetEmails.includes(email)) return ctx.reply('❌ Email sudah ada.');
    data.targetEmails.push(email);
    saveData();
    ctx.reply(`✅ ${email} ditambahkan ke target.`);
});

bot.command('deltargetemail', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /deltargetemail email');
    const email = args[1];
    const idx = data.targetEmails.indexOf(email);
    if (idx === -1) return ctx.reply('❌ Email tidak ditemukan.');
    data.targetEmails.splice(idx, 1);
    saveData();
    ctx.reply(`✅ ${email} dihapus dari target.`);
});

bot.command('setch', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /setch @ch1 @ch2');
    data.lockedChannels = args.slice(1);
    saveData();
    ctx.reply(`✅ Channel terkunci: ${data.lockedChannels.join(', ')}`);
});

bot.command('delch', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    data.lockedChannels = [];
    saveData();
    ctx.reply('✅ Semua kunci channel dihapus.');
});

bot.command('addredeem', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /addredeem kode');
    const result = createRedeemCode(args[1]);
    ctx.reply(result.message);
});

bot.command('delredeem', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    const args = ctx.message.text.split(' ');
    if (args.length < 2) return ctx.reply('❌ /delredeem kode');
    const result = deleteRedeemCode(args[1]);
    ctx.reply(result.message);
});

bot.command('listemail', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    if (!data.emails.length) return ctx.reply('📭 Belum ada email.');
    let msg = '📧 *Daftar Email Pengirim:*\n';
    data.emails.forEach((e, i) => msg += `${i+1}. ${e.user}\n`);
    ctx.replyWithMarkdown(msg);
});

bot.command('listtarget', (ctx) => {
    if (ctx.from.id !== ADMIN_ID) return ctx.reply('⛔ Admin only.');
    if (!data.targetEmails.length) return ctx.reply('📭 Belum ada target.');
    let msg = '📤 *Daftar Email Tujuan:*\n';
    data.targetEmails.forEach((e, i) => msg += `${i+1}. ${e}\n`);
    ctx.replyWithMarkdown(msg);
});

// ============================================================
//  ACTION BUTTON (semua dengan verifikasi)
// ============================================================
bot.action('change_email', ensureVerified, async (ctx) => {
    const userId = ctx.from.id;
    const user = getUser(userId);
    if (!user.isPremium) {
        ctx.answerCbQuery('⛔ Hanya Premium');
        return ctx.reply('⛔ Fitur ini hanya untuk Premium.');
    }
    ctx.answerCbQuery();
    ctx.deleteMessage().catch(() => {});
    if (data.emails.length === 0) return ctx.reply('❌ Belum ada email.');
    let msg = '📧 *Pilih email pengirim untuk laporan & tag scam:*\n\n';
    const buttons = [];
    data.emails.forEach((acc, i) => {
        const selected = (user.preferredEmail === i) ? ' ✅' : '';
        msg += `${i+1}. ${acc.user}${selected}\n`;
        buttons.push(Markup.button.callback(`${i+1}. ${acc.user}`, `select_email_${i}`));
    });
    buttons.push(Markup.button.callback('🔙 Pakai Default', 'use_default_email'));
    buttons.push(Markup.button.callback('❌ Batal', 'cancel_email'));
    const emailKeyboard = Markup.inlineKeyboard(buttons.map(b => [b]));
    ctx.replyWithMarkdown(msg, emailKeyboard);
});

bot.action(/select_email_(\d+)/, ensureVerified, async (ctx) => {
    const userId = ctx.from.id;
    const user = getUser(userId);
    if (!user.isPremium) return ctx.reply('⛔ Hanya Premium.');
    const idx = parseInt(ctx.match[1]);
    if (idx < 0 || idx >= data.emails.length) return ctx.reply('❌ Index tidak valid.');
    user.preferredEmail = idx;
    saveData();
    ctx.answerCbQuery(`✅ Email ${data.emails[idx].user} dipilih`);
    ctx.deleteMessage().catch(() => {});
    ctx.reply(`✅ Email pengirim diatur ke ${data.emails[idx].user} untuk semua laporan dan tag scam.`);
    ctx.reply('🏠 Kembali ke menu', mainMenu(true));
});

bot.action('use_default_email', ensureVerified, async (ctx) => {
    const userId = ctx.from.id;
    const user = getUser(userId);
    if (!user.isPremium) return ctx.reply('⛔ Hanya Premium.');
    user.preferredEmail = null;
    saveData();
    ctx.answerCbQuery('✅ Menggunakan default');
    ctx.deleteMessage().catch(() => {});
    ctx.reply(`✅ Sekarang menggunakan email default (${data.emails[data.defaultEmailIndex]?.user || 'pertama'}).`);
    ctx.reply('🏠 Kembali ke menu', mainMenu(true));
});

bot.action('cancel_email', ensureVerified, async (ctx) => {
    ctx.answerCbQuery('Dibatalkan');
    ctx.deleteMessage().catch(() => {});
    ctx.reply('❌ Perubahan email dibatalkan.');
});

bot.action('cancel_tag', ensureVerified, async (ctx) => {
    ctx.answerCbQuery('Dibatalkan');
    ctx.deleteMessage().catch(() => {});
    ctx.reply('❌ Tag scam dibatalkan.');
});

bot.action('menu', ensureVerified, async (ctx) => {
    ctx.answerCbQuery();
    ctx.deleteMessage().catch(() => {});
    bot.start(ctx);
});

bot.action('report', ensureVerified, async (ctx) => {
    ctx.answerCbQuery();
    ctx.deleteMessage().catch(() => {});
    ctx.reply('📝 Kirim laporan dengan perintah:\n/report @username ID');
});

bot.action('claim', ensureVerified, async (ctx) => {
    ctx.answerCbQuery();
    ctx.deleteMessage().catch(() => {});
    bot.command('claim', ctx);
});

bot.action('redeem', ensureVerified, async (ctx) => {
    ctx.answerCbQuery();
    ctx.deleteMessage().catch(() => {});
    ctx.reply('🔑 Masukkan kode redeem:\n/redeem KODE');
});

bot.action('status', ensureVerified, async (ctx) => {
    ctx.answerCbQuery();
    ctx.deleteMessage().catch(() => {});
    bot.command('status', ctx);
});

bot.action('help', ensureVerified, async (ctx) => {
    ctx.answerCbQuery();
    ctx.deleteMessage().catch(() => {});
    bot.help(ctx);
});

bot.action('scam_tag', ensureVerified, async (ctx) => {
    ctx.answerCbQuery();
    ctx.deleteMessage().catch(() => {});
    bot.command('scam_tag', ctx);
});

// ============================================================
//  ACTION CONFIRM — dengan notifikasi jelas
// ============================================================
bot.action('confirm_yes', ensureVerified, async (ctx) => {
    ctx.answerCbQuery();
    const userId = ctx.from.id;
    const session = userSession.get(userId);
    if (!session || session.step !== 'confirm') {
        return ctx.reply('⚠️ Sesi tidak valid. Mulai /report');
    }

    try {
        // Kurangi limit hanya sekali
        if (userId !== ADMIN_ID) {
            const user = getUser(userId);
            if (user.limit < 0) {
                return ctx.reply('❌ Limit tidak mencukupi.');
            }
        }

        const loopCount = session.data.loopCount || 1;
        const delaySeconds = session.data.delaySeconds || 5;

        await ctx.reply(`⏳ Mengirim laporan sebanyak ${loopCount} kali dengan jeda ${delaySeconds} detik...`);

        const result = await sendReportLoop(userId, session.data);

        // Tambahkan total laporan ke statistik
        data.totalReports += loopCount;
        saveData();

        let msg = `📤 *Hasil Pengiriman (${loopCount} kali loop)*\n\n`;
        msg += `${result.summary}\n\n`;
        result.allResults.forEach(r => {
            msg += `Loop #${r.loop}: ${r.message}\n`;
        });
        msg += `\n💳 Sisa limit: ${userId === ADMIN_ID ? '∞' : getUser(userId).limit}`;

        await ctx.replyWithMarkdown(msg, afterReportKeyboard);
        console.log(`[LOG] ${session.data.reporter} -> ${session.data.username} (${loopCount} loop, total success ${result.overallSuccess})`);
        userSession.delete(userId);
    } catch (err) {
        console.error('❌ Error saat mengirim laporan:', err);
        // Kirim pesan umum ke user, error detail hanya di console
        ctx.reply('❌ Gagal mengirim laporan. Coba lagi nanti.').catch(() => {});
        userSession.delete(userId);
    }
});

bot.action('confirm_no', ensureVerified, (ctx) => {
    ctx.answerCbQuery();
    ctx.deleteMessage().catch(() => {});
    ctx.reply('❌ Laporan dibatalkan.', afterReportKeyboard);
    userSession.delete(ctx.from.id);
});

// ============================================================
//  HANDLE PESAN TEKS (alur report dengan loop & delay)
// ============================================================
bot.on('text', async (ctx) => {
    const userId = ctx.from.id;
    const session = userSession.get(userId);
    if (!session) return;

    const text = ctx.message.text.trim();

    // ALUR SCAM TAG (PREMIUM)
    if (session.step === 'scam_tag_username') {
        const channel = text;
        const tag = `
🏷️ *TAG SCAM CHANNEL — GRENXHARIMAU EDITION*
Channel : ${channel}
Pelapor : ${session.data.reporter}
Tanggal : ${new Date().toLocaleString('id-ID')}

⚠️ *PERINGATAN:* Channel ini terbukti scam!  
Laporkan segera! #GrenXHarimau #AntiScam
        `;
        await ctx.replyWithMarkdown(tag);
        ctx.reply('✅ Tag scam berhasil!', afterReportKeyboard);
        userSession.delete(userId);
        return;
    }

    // ALUR REPORT BIASA
    switch (session.step) {
        case 'username':
            session.data.username = text;
            session.step = 'type';
            ctx.reply('☠️ Tipe scam:\n`bot`, `channel`, `group`, `user`, `phishing`');
            break;

        case 'type': {
            const valid = ['bot', 'channel', 'group', 'user', 'phishing'];
            if (!valid.includes(text.toLowerCase())) {
                return ctx.reply('❌ Tipe tidak valid. Pilih: bot, channel, group, user, phishing');
            }
            session.data.type = text.toLowerCase();
            session.step = 'description';
            ctx.reply('📝 Deskripsi lengkap (bukti, modus, dll):');
            break;
        }

        case 'description':
            session.data.description = text;
            session.step = 'loop';
            ctx.reply('🔄 Berapa kali laporan akan dikirim? (1-10, default 1)\nKetik angka atau kirim "1" untuk default.');
            break;

        case 'loop': {
            let loop = parseInt(text);
            if (isNaN(loop) || loop < 1) loop = 1;
            if (loop > 10) loop = 10;
            session.data.loopCount = loop;
            session.step = 'delay';
            ctx.reply(`⏱️ Berapa detik jeda antar pengiriman? (1-60, default 5)\nKetik angka atau kirim "5" untuk default.`);
            break;
        }

        case 'delay': {
            let delay = parseInt(text);
            if (isNaN(delay) || delay < 1) delay = 5;
            if (delay > 60) delay = 60;
            session.data.delaySeconds = delay;
            session.step = 'confirm';

            const summary = `
📋 *Ringkasan Laporan*
Username  : ${session.data.username}
Tipe      : ${session.data.type}
Deskripsi : ${session.data.description.substring(0, 100)}${session.data.description.length > 100 ? '...' : ''}
Loop      : ${session.data.loopCount} kali
Jeda      : ${session.data.delaySeconds} detik

Klik tombol di bawah untuk mengirim atau membatalkan.`;
            await ctx.replyWithMarkdown(summary, confirmKeyboard);
            break;
        }

        default:
            ctx.reply('⚠️ Sesi tidak valid. Mulai /report');
            userSession.delete(userId);
    }
});

// ============================================================
//  GLOBAL ERROR HANDLER & LAUNCH
// ============================================================
bot.launch({ timeout: 120000, allowedUpdates: ['message', 'callback_query'] })
    .then(() => console.log('🤖 MURTAG FREE VVIP Bot berjalan...'))
    .catch(err => {
        console.error('❌ Launch error:', err);
        setTimeout(() => bot.launch(), 5000);
    });

process.once('SIGINT', () => { saveData(); bot.stop('SIGINT'); });
process.once('SIGTERM', () => { saveData(); bot.stop('SIGTERM'); });

process.once('SIGINT', () => { saveData(); bot.stop('SIGINT'); });
process.once('SIGTERM', () => { saveData(); bot.stop('SIGTERM'); });