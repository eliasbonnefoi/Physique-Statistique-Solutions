# TP Physique Statistique Appliquée — Solutions, dispersions et hydrogel

Elias Bonnefoi — ESPCI Paris PSL, 1ère année (2025-2026)
Binôme : Félix Clavier (Parties A & B), Maxime Rimbaud (Partie C)

Ce TP étudie trois systèmes modèles de complexité croissante en physique statistique des
solutions : le gonflement osmotique d'un hydrogel, la diffusion brownienne de colloïdes, et
la double couche électrique à une interface chargée. Chaque partie est un dossier
indépendant, organisé selon la même convention : `Python/` (scripts d'analyse), `Data/`
(données mesurées) et `Images/` (figures produites) — voir la structure ci-dessous.

## Structure du dépôt

```
├── rapport.pdf                          compte-rendu complet (22 pages)
│
├── partie_A_gonflement_hydrogel/        gonflement osmotique de billes d'alginate
│   ├── notes.txt                        vue d'ensemble de la partie
│   ├── Python/                          plot concentration calcium.py, plot concentration temps.py, untitled1.py
│   ├── Images/                          graphiques de synthèse (toutes conditions confondues)
│   └── Data/                            une mesure par condition (Results.csv + notes.txt),
│                                         + suivi temporel de la synérèse
│
├── partie_B_diffusion_colloides/        mouvement brownien de colloïdes
│   ├── notes.txt                        vue d'ensemble de la partie
│   └── Data/                            observations microscope, tracking de particules
│                                         (_spots.csv, .fig, .sfit), profil de concentration
│
└── partie_C_double_couche_electrique/   double couche électrique graphite/électrolyte
    ├── notes.txt                        vue d'ensemble de la partie
    ├── Python/                          plot capacite vs concentration.py
    └── Images/                          charge_vs_tension.png, capacite_vs_concentration.png
```

Chaque dossier et sous-dossier contient un `notes.txt` qui explique son contenu et la
notation des données (colonnes des `.csv`, unités, provenance des mesures).

## Partie A — Gonflement osmotique d'un hydrogel

Des billes d'alginate de sodium sont formées par gélification ionique dans du CaCl₂, puis mises à l'équilibre dans des solutions de concentration croissante en Ca²⁺ (0 à 50 mM). À l'équilibre thermodynamique, la pression osmotique totale (mélange + élasticité du réseau + contribution ionique) s'annule. Le rayon des billes présente un minimum autour d'une **concentration critique de 20 mM**, avant de raugmenter aux fortes concentrations. La synérèse (expulsion d'eau) est également suivie au cours du temps et modélisée par une décroissance exponentielle `R(t) = a·exp(-bt) + c`.

## Partie B — Diffusion de colloïdes

Des colloïdes de silice (5 µm) et de latex (1,5 µm) sont observés au microscope pour étudier leur mouvement brownien. Le diamètre caractéristique du régime colloïdal est retrouvé en égalant l'énergie d'agitation thermique `k_BT` à l'énergie potentielle de pesanteur apparente sur une échelle égale à la taille de la particule. Les trajectoires (petit et grand ROI) permettent d'extraire un coefficient de diffusion `D = (8,12 ± 0,8) × 10⁻¹³ m²/s`, cohérent avec la prédiction de Stokes-Einstein (`4,77 × 10⁻¹³ m²/s`).

## Partie C — Double couche électrique

Un assemblage de plaques de graphite est immergé dans une solution de NaCl. La chrono-ampérométrie et la voltamétrie cyclique permettent de mesurer la capacité différentielle du système (modélisé comme deux capacités en série : couche de Stern et couche diffuse de Gouy-Chapman) à différentes concentrations ioniques, et d'en extraire la **longueur de Debye** `λ_D`. La loi d'échelle `1/C ∝ 1/√c₀` prédite par la théorie est retrouvée expérimentalement (pente mesurée 1,77 F⁻¹·M^(1/2) contre 0,71 F⁻¹·M^(1/2) en théorie, l'écart étant attribué à la couche de Stern négligée).

## Remarque sur les données

Les images brutes de microscopie (~1700 fichiers `.tiff`, ~660 Mo) ne sont **pas incluses** dans ce dépôt (trop volumineuses pour git). Seuls le code d'analyse, les données extraites (`Results.csv`, `_spots.csv`) et les figures produites sont versionnés — voir le `notes.txt` de chaque dossier concerné.

## Dépendances

```bash
pip install numpy matplotlib scipy
```
