# Network Scanner

Bu dastur tarmoqdagi barcha **aktiv IP-larni** va **ochiq portlarni** skanerlaydi.

## 📥 O‘rnatish
1. **Python 3** o‘rnatilganligini tekshiring.
2. Terminal yoki CMD ochib quyidagi buyruqni bajaring:
   ```sh
   git clone https://github.com/yourusername/NetworkScanner.git
   cd NetworkScanner
   ```
   
## 🚀 Ishga tushirish
1. Dastur katalogiga kiring:
   ```sh
   cd NetworkScanner
   ```
2. Dasturni ishga tushiring:
   ```sh
   python network_scanner.py
   ```

## 🔍 Xususiyatlari
- **Tarmoqdagi barcha aktiv IP-larni aniqlaydi** (ping orqali)
- **Faol IP-lardagi ochiq portlarni tekshiradi** (22, 23, 80, 443, 3389)
- **Tez ishlaydi** (multithreading bilan)
