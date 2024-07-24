# JWT_Auth
JWT Authentication

JWT (JSON Web Token) token — bu JSON formatida saqlanadigan xavfsizlik tokenidir. U web ilovalarda autentifikatsiya va autorizatsiya maqsadida keng qo'llaniladi. JWT asosan uch qismdan iborat: Header (Sarlavha), Payload (Yuk), va Signature (Imzo).

# JWT ning Tuzilishi
1. Header (Sarlavha): Sarlavhada tokenning turi (JWT) va ishlatilgan shifrlash algoritmi (masalan, HS256 yoki RS256) haqida ma'lumot mavjud.

2. Payload (Yuk): Yuk qismida foydalanuvchining ma'lumotlari va boshqa qo'shimcha ma'lumotlar (claims) mavjud. Bu ma'lumotlar odatda sub (foydalanuvchi identifikatori), iat (token chiqarilgan vaqt), exp (tokenning amal qilish muddati), va boshqalarni o'z ichiga oladi.

3. Signature (Imzo): Imzo qismi header va payload qismlarini birgalikda shifrlash orqali hosil qilinadi. Bu tokenning haqiqiyligini va uni hech qanday o'zgartirishlar kiritilmaganligini

# JWT ning Avzalliklari
1. Stateless (Shtatsiz): JWT tokenlarida foydalanuvchi ma'lumotlari saqlanadi, bu esa server tomonidan sessiya ma'lumotlarini saqlashni talab qilmaydi. Bu shtatsiz autentifikatsiya tizimlarini qo'llashga imkon beradi.

2. Shkalalanish: JWT statelessligi sababli, uni turli serverlar orasida oson ko'paytirish (scale) mumkin. Bu bir nechta serverlarda ishlayotgan ilovalar uchun juda foydali.

3. Ochiqlik va Standartlashtirilgan: JWT JSON formatida bo'lib, uni o'qish va tekshirish oson. JWT ochiq standarti bo'lgani uchun, u turli platformalar va texnologiyalar o'rtasida muammosiz ishlaydi.

4. Himoya va Xavfsizlik: JWT imzosi tokenning o'zgartirilmaganligini ta'minlaydi. Shuningdek, JWT ning o'zi shifrlanmagan bo'lsa-da, transport qatlamida (masalan, HTTPS orqali) himoyalanishi kerak.

5. Qo'shimcha Ma'lumotlar Saqlash Imkoni: JWT payload qismiga kerakli bo'lgan qo'shimcha ma'lumotlarni joylashtirish mumkin, bu esa ilovalarning yanada ko'p vazifalarni bajarishiga imkon beradi.

## JWT autentifikatsiya tizimlarida foydalanuvchilarni tekshirish va ruxsatlarni boshqarish uchun keng qo'llaniladi. Ular web ilovalar, mobil ilovalar va mikroxizmatlar arxitekturasida ishlatilishi mumkin.