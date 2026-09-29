# TP Physique Statistique Appliquée — Solutions & Dispersions

Elias Bonnefoi & Clavier — ESPCI Paris PSL, 1ère année (2025-2026)

## Contenu

Le TP se déroule en 3 séances, chacune dans son propre dossier :

- **Séance 1** — synérèse de billes d'alginate de calcium : effet de la concentration en CaCl₂ et en NaCl sur le rayon des billes, suivi temporel de la synérèse.
  - `plot concentration calcium.py` — rayon en fonction de la concentration en calcium
  - `plot concentration temps.py` — modélisation exponentielle de la synérèse `R(t) = a·exp(-bt) + c` (régression + R²)
  - `untitled1.py` — évolution du rayon au cours du temps (mesure complémentaire)
  - dossiers par condition (`5/10/20/30/50 mM CaCl2`, `50 NaCl`, `Eau`) — résultats de suivi d'image (`Results.csv`)
  - `Résultats toute parties.xlsx`, `Rayon toutes parties.png` — synthèse toutes conditions confondues

- **Séance 2** — suivi de colloïdes (silice, latex) par tracking de particules : `_spots.csv` (positions détectées), fichiers `.fig` (figures MATLAB), `.sfit` (modélisation de diffusion).

- **Séance 3** — mesures de capacité en fonction de la concentration ionique (`script.py`), tracé de `1/C` en fonction de `1/√Concentration` (loi de type Gouy-Chapman).

## Remarque sur les données

Les images brutes de microscopie (~1700 fichiers `.tiff`, ~660 Mo) ne sont **pas incluses** dans ce dépôt (trop volumineuses pour git). Seuls le code d'analyse, les données extraites (`Results.csv`, `_spots.csv`) et les figures produites sont versionnés.

## Dépendances

```bash
pip install numpy matplotlib scipy
```
