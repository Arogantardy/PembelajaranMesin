1. Komponen Kamus Data Klinis (Data Dictionary)
Setiap parameter di bawah ini diambil dari fluida serum darah pasien dan memiliki fungsi khusus dalam memetakan stadium penyakit hati:
1.Category (Target Utama)
-Tipe Data: Kualitatif (Nominal)
-Batas Rentang: 0=Blood Donor (Sehat), 0s=suspect Blood Donor, 1=Hepatitis, 2=Fibrosis, 3=Cirrhosis
-Deskripsi Klinis: Label diagnosis tingkat perkembangan atau stadium kerusakan fungsional pada jaringan parenkim organ hati pasien.

2.Age
-Tipe Data: Kuantitatif (Diskrit)
-Satuan Medis: Tahun
-Deskripsi Klinis: Usia biologis pasien saat proses pengambilan sampel darah dan diagnosis laboratorium dilakukan.

3.Sex
-Tipe Data: Kualitatif (Nominal)
-Kategori: m (Laki-laki), f (Perempuan)
-Deskripsi Klinis: Jenis kelamin biologis pasien yang nantinya ditransformasikan menjadi biner (1 dan 0) pada tahapan preprocessing data pipeline.

4.ALB (Albumin)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: g/L (gram per Liter)
-Rentang Normal: 35 – 52 g/L
-Deskripsi Klinis: Protein utama hasil sintesis hati. Kadarnya akan menurun tajam (hipoalbuminemia) pada penderita stadium kronis seperti Sirosis akibat rusaknya sel pembuat protein.

5.ALP (Alkaline Phosphatase)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: U/L (Unit per Liter)
-Rentang Normal: 30 – 120 U/L
-Deskripsi Klinis: Enzim yang melekat erat pada dinding saluran empedu. Mengalami lonjakan signifikan jika terjadi kolestasis atau obstruksi (sumbatan) empedu.

6.ALT (Alanine Aminotransferase)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: U/L (Unit per Liter)
-Rentang Normal: 7 – 56 U/L
-Deskripsi Klinis: Enzim yang paling spesifik berada di dalam sel hati (hepatosit). Enzim ini akan bocor masif ke aliran darah jika terjadi peradangan akut atau nekrosis (kematian sel) hati.

7.AST (Aspartate Aminotransferase)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: U/L (Unit per Liter)
-Rentang Normal: 10 – 40 U/L
-Deskripsi Klinis: Enzim yang ditemukan pada hati, jantung, dan otot. Evaluasi rasio antara AST dan ALT (Rasio De Ritis) jika melebihi angka 1 merupakan indikator kuat bahwa kerusakan hati telah berkembang ke arah Sirosis berat.

8.BIL (Bilirubin)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: µmol/L (Mikromol per Liter)
-Rentang Normal: 1.7 – 22 µmol/L
-Deskripsi Klinis: Pigmen kuning sisa pemecahan sel darah merah tua oleh limpa. Akumulasi bilirubin akibat kegagalan fungsi filter hati akan memicu manifestasi klinis penyakit kuning (jaundice).

9.CHE (Cholinesterase)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: kU/L (Kilo-Unit per Liter)
-Rentang Normal: 5.3 – 12.9 kU/L
-Deskripsi Klinis: Parameter sensitif untuk mengukur kapasitas sintesis fungsional dari parenkim hati yang masih tersisa. Kadarnya merosot drastis seiring tingkat keparahan disfungsi organ kronis.

10.CHOL (Cholesterol)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: mmol/L (Millimol per Liter)
-Rentang Normal: 3.6 – 5.2 mmol/L
-Deskripsi Klinis: Senyawa lipid yang diproduksi dan dimetabolisme oleh organ hati. Digunakan untuk memantau integritas regulasi metabolisme lemak tubuh secara general.

11.CREA (Creatinine)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: µmol/L (Mikromol per Liter)
-Rentang Normal: 62 – 115 µmol/L
-Deskripsi Klinis: Indikator fungsi filtrasi ginjal. Pemantauan nilai ini sangat vital bagi pasien sirosis hati stadium lanjut karena mereka berisiko tinggi mengalami komplikasi fatal berupa penurunan fungsi ginjal akut (Sindrom Hepatorenal).

12.GGT (Gamma-Glutamyl Transferase)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: U/L (Unit per Liter)
-Rentang Normal: 8 – 61 U/L
-Deskripsi Klinis: Penanda enzimatis yang sangat sensitif terhadap kerusakan sel hati akibat pengaruh luar seperti induksi alkohol, paparan zat toksik, atau konsumsi obat-obatan jangka panjang.

13.PROT (Total Protein)
-Tipe Data: Kuantitatif (Kontinu)
-Satuan Medis: g/L (gram per Liter)
-Rentang Normal: 60 – 80 g/L
-Deskripsi Klinis: Akumulasi total dari protein serum global (gabungan Albumin dan Globulin) di dalam darah untuk mengevaluasi status nutrisi serta kemampuan sintesis tubuh secara menyeluruh.