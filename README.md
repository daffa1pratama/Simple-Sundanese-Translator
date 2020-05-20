# Simple Sundanese Translator
Simple Sundanese to Bahasa Indonesia translator using Pattern Matching

## Latar Belakang
Pada suatu hari, ada mahasiswa bernama Riyugan yang baru pindah ke Bandung. Pada awalnya dia mengalami kesulitan untuk bersosialisai dengan lingkungan sekitar karena orang-orang di lingkungannya yang baru hanya berbicara dalam bahasa Sunda. Beruntungnya Riyugan punya teman dari kampung halamannya, yaitu Anda, untuk diminta membuat penerjemah sederhana dari Bahasa Sunda ke Bahasa Indonesia begitu pula sebaliknya untuk memudahkan dirinya bersosialisasi dengan lingkungan barunya di Bandung.

## Deskripsi
Program Simple Sundenese Translator adalah sebuah program sederhana berbasis website yang berguna untuk menerjemahkan kalimat berbahasa Indonesia ke bahasa Sunda ataupun sebaliknya. Program ini dapat menghapus dan menambahkan partikel penegas 'Teh' dalam bahasa Sunda. Pengguna dapat memilih algoritma pencocokan string yang digunakan, tersedia algoritma Knuth-Morris-Pratt (KMP), algoritma Boyer-Moore (BM), dan Regular Expression (Regex). Pengguna juga dapat memilih metode pencarian kata yang digunakan, tersedia pilihan cari semua kata yang cocok dalam kamus atau kata pertama yang ditemukan.

## Fitur Tambahan
Developer menambahkan fitur metode pencarian, tersedia pilihan FindAll atau FindFirst. Fitur ini ditambahkan karena ada beberapa kalimat yang jika diterjemahkan menjadi kalimat yang tidak lazim digunakan. Seperti contoh :
```
Sunda - Indonesia
Sunda : abdi jalma Surabaya
Indonesia (FindFirst) : saya manusia Surabaya
Indonesia (FindAll) : saya manusia/orang Surabaya
```
Fitur ini ditambahkan dengan harapan pengguna dapat memilih pilihan kata terjemahan yang diberikan oleh program

## Getting Started
### Prerequisites
Hal yang perlu dipersiapkan untuk menjalankan program ini :
```
- Python Compiler (versi 3.x.x)
- Web Browser
- Web Server
```
Langkah-langkah yang harus dilakukan untuk memenuhi prerequisites di atas adalah sebagai berikut :
1. Install Python Compiler (versi 3.x.x) dengan mengunduh dari laman :
```
https://www.python.org/downloads/
```
2. Install web browser, dibebaskan. Developer menggunakan google chrome yang dapat diunduh dari laman :
```
https://www.google.com/intl/id_id/chrome/
```
3. Install web server, dibebaskan. Developer menggunakan XAMPP yang dapat diunduh dari laman :
```
https://www.apachefriends.org/index.html
```

### Installing
Berikut adalah langkah-langkah untuk menginstall program :
1. Copy folder `Simple-Sundanese-Translator`
2. Paste pada direktori `C:\xampp\htdocs\`
3. Jalankan XAMPP
4. Jalankan module Apache pada XAMPP
5. Masukkan alamat `http://localhost/Simple-Sundanese-Translator/src/` pada web browser
6. Program berhasil dijalankan

## Tests
```
Sunda - Indonesia
Sunda : nami abdi Riyugan
Indonesia : nama saya Riyugan
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : nama saya Riyugan
Sunda : nami abdi Riyugan
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi henteu tiasa bahasa Sunda
```
## Tampilan Program


## Built With
* [Bootstrap](https://getbootstrap.com/) - Layouting website
* [SB Admin 2](https://startbootstrap.com/themes/sb-admin-2/) - Bootstrap template
* [Python](https://www.python.org/) - Backend
* [PHP] - Backend

## Catatan
 - Kamus yang digunakan pada program ini tidak sepenuhnya mencakup kosakata bahasa Sunda dan bahasa Indonesia, sehingga ada kata-kata yang gagal diterjemahkan karena kurangnya kosakata dalam kamus.
 - Program hanya dapat membaca kata yang diterjemahkan dalam lowercase, sehingga kata yang tidak dalam lowercase tidak dapat diterjemahkan dan dianggap sebagai kata diluar kamus.

## Author
**Daffa Pratama Putra / 13518033** - *Programmer, Tester*