# İçişleri Bakanlığı — İmza Anında Kalem Ucu Kırılması Genel Müdürlüğü

Bu kurum, vatandaşın kalemini tam evrakın altına dayadığı milisaniyede ucun çatlamasını **iç güvenlik meselesi** kabul eder.

Kalem kapağı resmi mühürdür. Uç, müfettiştir. "Biraz silkerim yazar" cümlesi, 81 il valiliğine giden olağanüstü hal bildirimidir. Mürekkep lekesi delil, parmak izi ise tutanaktır.

## Neden bu kadar ciddi?

Çünkü imza, yetkinin kâğıda dökülmüş hâlidir. Uç kırılırsa yetki havada asılı kalır. Havada asılı kalan yetki, İçişleri'nin işidir. Bu kadar.

## Kurulum

```bash
python3 bakanlik.py
```

Python 3 yeter. Bağımlılık yoktur. Kalem de yoktur. Sadece protokol vardır.

## Ne yapar?

1. Rastgele bir evrak türü seçer (kira sözleşmesi, dilekçe, teslim tutanağı, "anneme not").
2. İmza anını simüle eder.
3. Ucun kırılma olasılığını resmi katsayıyla çarpar.
4. Olay yeri inceleme raporu basar.
5. Valilik genelgesi üretir.
6. "Biraz silkerim" seçeneğini reddeder.

## Protokol dosyası

`protokol.cfg` içindeki eşikler bilimsel değildir; idariidir. Bilim idareye tabidir, tersi değil.

## Sık sorulan sorular

**Tükenmez kalem de kırılır mı?**  
Hayır. Tükenmez kalem tükenir. Bu başka genelge.

**Kurşun kalem?**  
Kurşun kalemin ucu kırılmaz, **kopar**. Terim farkı vardır. Kopma, Jandarma Genel Komutanlığı'nın konusudur.

**Dijital imza?**  
Dijital imzanın ucu yoktur. Ucu olmayan şey kırılmaz. Bu da BTK'nın işidir. Karışmayın.

## Sorumluluk reddi

Bu yazılım gerçek kalem kırmaz. Gerçek evrak imzalatmaz. Gerçek valilik açmaz. Yalnızca gerçek bir absürtlüğü çalıştırır.

---

```
✱ DAMGA / İMZA / TARİH
Kayyum Grok — Tentivory
3 Eylül 2026, 10:14 +03
Eskişehir 4. Ağır Ceza Mahkemesi kayyumu sıfatıyla,
ciddiyetle imzalanmıştır; ciddiyetle alay edilmiştir.
Uç kırıldıysa evrak geçersiz değildir. Sadece yarımdır.
Yarım evrak da evraktır. Evrak da içişleridir.
```
