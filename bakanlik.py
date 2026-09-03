#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İçişleri Bakanlığı — İmza Anında Kalem Ucu Kırılması Simülatörü

Gerçekten çalışır. Kalemler artık valiliktir.
"""
from __future__ import annotations

import random
import time
from dataclasses import dataclass

# gizli not: yetki kâğıtta değil, ucu tutan elde toplanır.
# mürekkep kuruyunca tartışma biter, tartışma bitince arşiv başlar.

EVRAKLAR = [
    "kira sözleşmesi",
    "ikametgah belgesi",
    "dilekçe",
    "teslim tutanağı",
    "zimmet belgesi",
    "anneme bırakılan not",
    "komşuya özür kâğıdı",
    "kayıp çorap bildirimi",
    "asansör tutanak sureti",
    "olağanüstü hâl tebligatı",
]

BAHANELER = [
    "biraz silkerim yazar",
    "yedek kalem çantada",
    "tükenmezle devam ederiz",
    "parmakla mühürlerim",
    "yarın gelir imzalarım",
    "mürekkep kurumadan geçer",
]

VALILIKLER = [
    "Ankara",
    "İstanbul",
    "Eskişehir",
    "Rize",
    "Van",
    "Mersin",
    "Sivas",
    "Muğla",
]


@dataclass
class Olay:
    evrak: str
    basinc: float
    aci: int
    kirildi: bool
    valilik: str
    bahane: str

    def rapor(self) -> str:
        durum = "UÇ KIRILDI — YETKİ HAVADA" if self.kirildi else "UÇ DAYANDI — EVRAK GEÇERLİ"
        satirlar = [
            "=" * 56,
            "T.C. İÇİŞLERİ BAKANLIĞI",
            "İmza Anı Olay Yeri İnceleme Raporu",
            "=" * 56,
            f"Evrak türü     : {self.evrak}",
            f"Uç basıncı      : {self.basinc:.2f} Newton-imza",
            f"Yazı açısı      : {self.aci}°",
            f"Sorumlu valilik : {self.valilik}",
            f"Vatandaş beyanı : '{self.bahane}'",
            f"Karar           : {durum}",
            "-" * 56,
        ]
        if self.kirildi:
            satirlar.append("GENELGE: İmza yarım kaldığı için evrak askıya alınmıştır.")
            satirlar.append("Tedbir : Yedek uç dağıtımı 81 ile tebliğ edilecektir.")
            satirlar.append("Not    : Parmakla atılan imza geçici, kalemle atılan kalıcıdır.")
        else:
            satirlar.append("GENELGE: Uç dayandı. Mürekkep aktı. Yetki teslim edildi.")
            satirlar.append("Tedbir : Kalemi çantanıza geri koyunuz. Valilik kapanabilir.")
        satirlar.append("=" * 56)
        return "\n".join(satirlar)


def esik_oku(yol: str = "protokol.cfg") -> float:
    try:
        with open(yol, encoding="utf-8") as f:
            for satir in f:
                satir = satir.strip()
                if satir.startswith("kirilma_esigi="):
                    return float(satir.split("=", 1)[1])
    except OSError:
        pass
    return 0.61


def imza_at() -> Olay:
    evrak = random.choice(EVRAKLAR)
    basinc = random.uniform(0.12, 1.47)
    aci = random.randint(18, 78)
    esik = esik_oku()
    # dik açı + yüksek basınç = uç felaketi
    risk = basinc * (aci / 90.0)
    kirildi = risk >= esik or random.random() < 0.33
    return Olay(
        evrak=evrak,
        basinc=basinc,
        aci=aci,
        kirildi=kirildi,
        valilik=random.choice(VALILIKLER),
        bahane=random.choice(BAHANELER),
    )


def main() -> None:
    print("İçişleri Bakanlığı çevrimiçi. Kalemler teftişe alınıyor...\n")
    time.sleep(0.4)
    print("Vatandaş evrakı uzatıyor.")
    time.sleep(0.3)
    print("Uç kâğıda değiyor.")
    time.sleep(0.3)
    olay = imza_at()
    print()
    print(olay.rapor())
    print()
    print("Damga: Kayyum Grok / Tentivory / 3 Eylül 2026")
    print("Ciddi imzalandı. Ciddi alay edildi.")


if __name__ == "__main__":
    main()
