# TER

## Slide 1

Bonjour, je m'appelle Adonis je suis étudiant en Master 1 CMI Image et je vais
vous présenter mon sujet de Travail d'Etude et de Recherche. J'étais encadré par
Mr. Antonio Capobianco et Mr. Flavien Lécuyer et je voudrais surtout les
remercier pour leur aide tout au long de ce travail.

## Slide 2

Mon sujet de TER porte sur l'analyse des données d'eye-tracking. Donc qu'est-ce
que l'eye-tracking? L'oculométrie, en français, est le processus ou un ensemble
de techniques qui permettent de suivre le regard d'un individu. Ce peut être
utilisé dans plusieurs domaines comme le marketing, pour déterminer les zones
les plus attirantes sur un support, une affiche publicitaire par exemple.

L'objectif de mon travail était de proposer un outil pour pouvoir analyser des
données récupérées durant des études d'eye-tracking. Ces études sont effectués
dans deux environnements différents : l'individu se place devant un écran et
l'observe pendant que l'on suit son regard.

Le deuxième environnement auquel on s'interesse est la réalité virtuelle.
L'individu porte un casque et il est plongé dans un scénario similaire : il se
trouve face à un écran et l'on s'intéresse à suivre son regard sur cet écran.
Vous pouvez voir ici un rendu de cet environnement utilisé pour l'étude en
réalité virtuelle.

## Slide 3

Pour avoir un peu plus de contexte et comprendre comment développer cet outil,
je vais d'abord parler des types de capteurs utilisés pour ces études, puis des
différents moyens d'analyser les données d'eye-tracking. Une partie de mon
travail était de trouver un outil permettant d'effectuer de l'analyse
d'oculométrie pour l'utiliser avec les données spécifiques à nos études. Je vais
donc parler un peu de quel logiciel j'ai utilisé et pourquoi. Enfin, je vais
présenter mon travail, comment j'ai implémenté mon outil et aussi les résultats
obtenus.

## Slide 4

Pour effectuer ces deux études il faut utiliser deux types de capteurs. Le
premier est un capteur pour écran : c'est une barre placée au dessus ou en
dessous d'un écran et observe les yeux de l'individu en face. Il peut donc
estimer la position du regard sur l'écran.

Pour l'étude dans l'environnement virtuel il faut utiliser un casque de réalité
virtuelle spécial avec des capteurs infrarouges intégrés. Ils premettraient
alors de suivre le regard dans environnement 3D. Donc notre étude, on
s'intéresse à suivre le regard sur un écran, donc ces positions 3D sont
traduites en des positions 2D sur l'écran virtuel.

## Slide 5

Maintenant que l'on sait comment sont récupérées les données, il faut comprendre
quel est le format de ces données. Une étude d'oculométrie, avec les capteurs
évoqués, nous permet de récupérer plusieurs informations. Mais la plus
importante est la position du regard sur l'écran. Avec un format comme celui-ci,
on peut déterminer la position du regard à un temps t d'une étude. L'unité de
ces valeurs peut varier : elles peuvent être en microsecondes, secondes pour le
temps, en pourcentages ou pixel pour les position. Il peut y avoir plusieurs
formats de données différents, mais les informations nécessaires sont surtout
ces trois valeurs.

Pour pouvoir analyser le regard et en tirer des conclusions pertinentes, il faut
trouver un bon support pour analyser les données récupérées par les études. On
pourrait afficher ces données avec des graphiques, mais comme les données
brutes, les valeurs numériques de positions sont difficiles à se représenter
dans un environnement à deux dimensions.

## Slide 6

Pour cela, la seconde solution seraient des représentations par cartes. On
pourrait par exemple représenter les positions du regard sur une capture de
l'écran. On peut ainsi proprement suivre le regard sur le contenu original assez
facilement. Cette représentation nous donne une idée assez claire du chemin du
regard de l'individu.

## Slide 7

On pourrait également réaliser des heatmaps, ou cartes de chaleurs. Elles
permettent d'indiquer les régions les plus visitées par le regard, et ainsi
distinguer les régions les plus attirantes. Comme sur cet exemple, on peut
très visiblement différencier les zones sur lesquel le regard s'est concentré
(en rouge) des régions qui les sont moins (en bleu). Il existe plein d'autres
formats de représentations des données qui pourraient aider à analyser le
regard, mais dans le cadre de ce travail je me suis contenté de se concentrer
sur ces deux spécialement.

## Slide 8

Avec toutes ces informations réunies j'ai une bonne idée à quoi m'attendre pour
développer mon outil. J'ai donc cherché si un logiciel d'analyse de données
d'eye-tracking existait déjà pour l'utiliser et m'aider à implémenter l'outil ou
sinon pour s'en inspirer. Il existe en fait plusieurs : GazePointer, Ogama,
PyGaze et GazeParser. Je les ai comparé sur les critères suivant : leur
flexibilité, c'est-a-dire la possibilité de modifier le code. GazePointer et
Ogama sont des applications et le code source n'est pas accessible. PyGaze et
GazeParser sont des bibliothèques et c'est donc plus facile de les ajouter à
l'outil directement. Le deuxième critère est le niveau d'analyse que chaque
logiciel propose. En général, tous les logiciels permettaient de créer des
supports d'analyse intéressants. Sinon, le critère final est la documentation et
la facilité d'utilisation. J'ai fini par choisir PyGaze car elle était la
meilleure bibliothèque dans l'ensemble et conviendrait bien pour ce travail.

## Slide 9

Pour implémenter alors mon outil il fallait prendre en compte le format des
données passées en entrée du programme. Deux formats m'étaient donnés pour deux
études différentes : la première étudie le regard sur un écran dans la vie
réelle et le second dans la réalité virtuelle. Ces formats contenaient les
mêmes informations mais sous la même forme. Aussi souvent ces données sont
volumineuses. Il faut donc d'abord réarranger ces données en un format que
l'outil comprendrait facilement où les données sont facilement compréhensibles.

Ainsi, j'ai opté pour le format suivant : c'est un fichier csv composé de deux
tableaux. Le premier indique l'image que l'individu observe et son temps
d'apparition dans l'expérience. Le second indique plusieurs autres données tels
que la position des fixations en X et Y, la distance entre l'individu et
l'écran et le diamètre de la pupille gauche et droite, en un instant t.

Pour réaliser alors les rendus des images analytiques, il faut d'abord regrouper
les informations par images : pour cela, j'ai utilisé l'indicateur de temps (les
deux premières lignes sont pour l'image1 et le reste pour la 2). Ensuite, je
passe les données des positions de fixations à la bibliothèque PyGaze, qui va
effectuer le rendu des cartes citées précédemment. La plupart du travail
consistait en de la manipulation de données pour les utiliser avec la
bibliothèque PyGaze.

## Slide 10

Donc pour les deux études concernées, j'ai eu les résultats suivants : pour
la première, j'ai la carte des points de fixations suivante. C'est un peu petit
mais on peut voir sur l'image plusieurs points indiquant que le regard s'est
concentré à cet endroit pendant une certaine période. Il faut noter, que cette
étude était effectué par une société tierce et que les données passées en entrée
étaient prétraitées pour transformer toutes les positions brutes en des groupes
proches dans l'espace et dans le temps en des points de fixations.

## Slide 11

Lorsqu'on observe la carte de chaleur de cette image, on aperçoit que les zones
les plus attirantes sont aussi les zones ou la densité de points est la plus
importante. J'ai eu un problème avec cette étude cependant, avec des valeurs de
défilement : en fait les images ici sont des pages web, et il fallait prendre
en compte une valeur de défilement de page pour déterminer la position exacte
des fixations. J'ai essayé mais j'ai pas réussi à la prendre en compte, donc les
fixations sont bien positionnées horizontalement mais pas forcément sur l'axe
vertical.

## Slide 12

Pour la deuxième étude, dans un environnement de réalité virtuelle j'ai eu des
résultats plus cohérents. Cette étude était menée dans le laboratore iCube avec
mes encadrants. L'individu devait se concentrer sur les informations importantes
d'affiches (titre, le lieu, l'organisateur, la date par exemple) et nous devons
être capables de distinguer ces informations à travers son regard. Avec cette
carte on voit bien que le regard permet de s'assimiler l'ensemble des ces
informations. Ici on voit beaucoup plus de points car un aucun traitement des
points n'a été fait au préalable.

## Slide 13

En observant la carte de chaleur de la même image on confirme que les zones
contenant les informations importantes sont celles qui ont attiré le plus le
regard. L'outil permet donc de donner des résultats cohérents avec les données
surtout pour des images fixes et on peut facilement comprendre le comportement
du regard d'un individu à travers ces rendus.

## Slide 14

Donc pour ce TER, j'ai réussi à développer un outil pour traiter les données
d'oculométrie, en traitant deux formats de données spécifiques. L'outil permet
de donner en sortie des images qui nous permettent de facilement comprendre ces
données.

Cependant, l'outil a ses limites : il manque certaines fonctionnalités comme
le traitement et le regroupement des fixations en des points de fixation ou le
défilement de pages web.

Avec plus de temps, j'aurais pu développer d'autres fonctionnalités pour pouvoir
prendre en compte plus de formats de données par exemple. L'étape d'après encore
serait de se baser sur cet outil en 2D pour effectuer des cartes d'analyse du
regard dans un environnement en 3 dimensions pour la réalité virtuelle.

Merci beaucoup!
