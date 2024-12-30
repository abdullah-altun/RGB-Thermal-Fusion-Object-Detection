# RGB-Thermal-Fusion-Object-Detection
Bu repository, RGB ve termal görüntülerin birleştirilerek nesne tespiti performansının artırılması için iki farklı yöntemin uygulanmasını sağlar: Target-aware Dual Adversarial Learning (TarDAL) ve SHIP yöntemleri.

## Genel Bakış
TarDAL ve SHIP yöntemleri, kızılötesi ve görünür görüntülerin modaliteler arasındaki benzerlikleri ve farklılıkları etkili bir şekilde birleştirmek için tasarlanmıştır. Bu yöntemler, kızılötesi görüntülerden yapısal bilgiyi ve görünür görüntülerden dokusal detayları koruyarak yüksek kaliteli füzyon elde etmeye odaklanır.

Repository şunları içerir:
- Görüntü füzyonu için TarDAL ve SHIP yöntemlerinin uygulaması.
- RGB ve termal görüntülerin birleştirildiği M3FD veri seti.
- RGB ve termal görüntülerin ayrı ayrı ve füzyonlanmış halleriyle yapılan nesne tespiti sonuçları.
- Sonuçların mevcut yöntemlerle karşılaştırıldığı benchmark değerlendirmeleri.
- Makaledeki sonuçları tekrar üretmek için kaynak kodu ve betikler.

## Özellikler
- **Yüksek Kaliteli Füzyon**: Daha iyi nesne tespiti için yüksek görsel kalitede birleştirilmiş görüntüler üretir.
- **Çok Yönlü Değerlendirme**: RGB ve termal görüntüler ayrı ayrı ve füzyonlanmış şekilde eğitilerek yöntemlerin performansı karşılaştırılır.

## Kullanılan Modeller ve Veri Seti
- **Veri Seti**: M3FD
- **Modeller**: YOLOv8m, YOLOv8x, YOLOv11m, YOLOv11x

## Eğitim Süreci
### 1. RGB ve Termal Görüntüler ile Eğitim
RGB ve termal görüntüler ayrı ayrı aşağıdaki modellerde eğitilmiştir:

| **Modality** | **Model**   | **mAP50** |
|--------------|-------------|-----------------------------|
| RGB          | YOLOv8m     | **0.764**                    |
| RGB          | YOLOv8x     | **0.768**                    |
| RGB          | YOLOv11m    | **0.749**                    |
| RGB          | YOLOv11x    | **TBD**                    |
| Thermal      | YOLOv8m     | **0.836**                    |
| Thermal      | YOLOv8x     | **TBD**                    |
| Thermal      | YOLOv11m    | **0.82**                    |
| Thermal      | YOLOv11x    | **TBD**                    |

### 2. Füzyon Yöntemleri ile Eğitim
TarDAL ve SHIP yöntemleriyle füzyonlanan görüntüler aşağıdaki modellerde eğitilmiştir:

| **Fusion Method** | **Model**   | **mAP50** |
|-------------------|-------------|-----------------------------|
| TarDAL            | YOLOv8m     | **0.833**                    |
| TarDAL            | YOLOv8x     | **TBD**                    |
| TarDAL            | YOLOv11m    | **TBD**                    |
| TarDAL            | YOLOv11x    | **TBD**                    |
| SHIP              | YOLOv8m     | **0.828**                    |
| SHIP              | YOLOv8x     | **TBD**                    |
| SHIP              | YOLOv11m    | **TBD**                    |
| SHIP              | YOLOv11x    | **TBD**                    |

## Kurulum
Bu repository'i klonlayın ve gerekli bağımlılıkları yükleyin:

```bash
git clone <repository-url>
pip install -r requirements.txt
```

## Teşekkür
"Target-aware Dual Adversarial Learning and a Multi-scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection" ve SHIP yönteminin yazarlarına temel yöntemler ve benchmarklar için teşekkür ederiz.
Daha fazla bilgi için [TarDAL GitHub repository](https://github.com/dlut-dimt/TarDAL) ve [SHIP GitHub repository](#) ziyaret edebilirsiniz.
