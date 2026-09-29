# TP Physique Statistique Appliquée — Solutions, dispersions et hydrogel

Elias Bonnefoi — ESPCI Paris PSL, 1ère année (2025-2026)
Binôme : Félix Clavier (Parties A & B), Maxime Rimbaud (Partie C)

## Contenu

- [`rapport.pdf`](rapport.pdf) — compte-rendu complet du TP
- [`partie_A_gonflement_hydrogel/`](partie_A_gonflement_hydrogel) — gonflement osmotique de billes d'alginate
- [`partie_B_diffusion_colloides/`](partie_B_diffusion_colloides) — mouvement brownien et diffusion de colloïdes
- [`partie_C_double_couche_electrique/`](partie_C_double_couche_electrique) — double couche électrique à l'interface graphite-électrolyte

Le TP étudie trois systèmes modèles de complexité croissante en physique statistique des solutions.

### Partie A — Gonflement osmotique d'un hydrogel

Des billes d'alginate de sodium sont formées par gélification ionique dans du CaCl₂, puis mises à l'équilibre dans des solutions de concentration croissante en Ca²⁺ (0 à 50 mM). À l'équilibre thermodynamique, la pression osmotique totale (mélange + élasticité du réseau + contribution ionique) s'annule. Le rayon des billes présente un minimum autour d'une **concentration critique de 20 mM**, avant de raugmenter aux fortes concentrations. La synérèse (expulsion d'eau) est également suivie au cours du temps et modélisée par une décroissance exponentielle `R(t) = a·exp(-bt) + c`.

- `plot concentration calcium.py` — rayon des billes en fonction de la concentration en Ca²⁺
- `plot concentration temps.py` — régression exponentielle de la synérèse
- `untitled1.py` — mesure complémentaire du rayon au cours du temps
- dossiers par condition (`5/10/20/30/50 mM CaCl2`, `50 NaCl`, `Eau`) — données de suivi d'image (`Results.csv`, issues d'ImageJ/Fiji)
- `Résultats toute parties.xlsx` — synthèse de toutes les conditions

### Partie B — Diffusion de colloïdes

Des colloïdes de silice (5 µm) et de latex (1,5 µm) sont observés au microscope pour étudier leur mouvement brownien. Le diamètre caractéristique du régime colloïdal est retrouvé en égalant l'énergie d'agitation thermique `k_BT` à l'énergie potentielle de pesanteur apparente sur une échelle égale à la taille de la particule. Les trajectoires (petit et grand ROI) permettent d'extraire un coefficient de diffusion `D = (8,12 ± 0,8) × 10⁻¹³ m²/s`, cohérent avec la prédiction de Stokes-Einstein (`4,77 × 10⁻¹³ m²/s`).

- dossiers `1000 img petit ROI` / `300 img grand roi` — tracking de particules (`_spots.csv`), figures MATLAB (`.fig`), modélisation (`.sfit`)
- dossiers `Colloide silice` / `Colloide latex` — observations préliminaires au microscope

### Partie C — Double couche électrique

Un assemblage de plaques de graphite est immergé dans une solution de NaCl. La chrono-ampérométrie et la voltamétrie cyclique permettent de mesurer la capacité différentielle du système (modélisé comme deux capacités en série : couche de Stern et couche diffuse de Gouy-Chapman) à différentes concentrations ioniques, et d'en extraire la **longueur de Debye** `λ_D`. La loi d'échelle `1/C ∝ 1/√c₀` prédite par la théorie est retrouvée expérimentalement (pente mesurée 1,77 F⁻¹·M^(1/2) contre 0,71 F⁻¹·M^(1/2) en théorie, l'écart étant attribué à la couche de Stern négligée).

- `script.py` — tracé de `1/C` en fonction de `1/√Concentration`

## Remarque sur les données

Les images brutes de microscopie (~1700 fichiers `.tiff`, ~660 Mo) ne sont **pas incluses** dans ce dépôt (trop volumineuses pour git). Seuls le code d'analyse, les données extraites (`Results.csv`, `_spots.csv`) et les figures produites sont versionnés.

## Dépendances

```bash
pip install numpy matplotlib scipy
```
