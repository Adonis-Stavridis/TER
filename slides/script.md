# TER

## Slide 1

Bonjour, je m'appelle Adonis je suis étudiant en Master 1 CMI Image et je vais
vous présenter mon sujet de Travail d'Etude et de Recherche. J'étais encadré par
Mr. Antonio Capobianco et Mr. Flavien Lécuyer et je voudrais surtout les
remercier pour leur aide tout au long de ce travail.

## Slide 2

Mon sujet de TER porte sur l'analyse des données d'eye-tracking. Donc qu'est-ce
que l'eye-tracking? L'oculométrie, en français, est le processus, un ensemble de
techniques, qui permettent de suivre le regard d'un individu. Ce peut être
utilisé dans plusieurs domaines comme le marketing, pour déterminer les zones
les plus attirantes sur un support, une affiche publicitaire par exemple.

L'objectif de mon travail était de proposer un outil pour pouvoir analyser des
données récupérées durant des études d'eye-tracking. Ces études sont effectués
dans deux environnements différents : l'individu se place devant un écran et
l'observe pendant que l'on suit son regard.

## Slide 3

Le deuxième environnement auquel on s'interesse est la réalité virtuelle.
L'individu porte un casque et il est plongé dans un scénario similaire : il se
trouve face à un écran et l'on s'intéresse à suivre son regard sur cet écran.
Vous pouvez voir ici un rendu de cet environnement utilisé pour l'étude en
réalité virtuelle.

## Slide 4

Pour avoir un peu plus de contexte et comprendre comment développer cet outil,
je vais d'abord parler des types de capteurs utilisés pour ces études, puis des
différents moyens d'analyser les données d'eye-tracking. Une partie de mon
travail était de trouver un outil permettant d'effectuer de l'analyse
d'oculométrie pour l'utiliser avec les données spécifiques à nos études. Je vais
donc parler un peu de quel logiciel j'ai utilisé et pourquoi. Enfin, je vais
présenter mon travail, comment j'ai implémenté mon outil et aussi les résultats
obtenus.

## Slide 5

Pour effectuer ces deux études il faut utiliser deux types de capteurs. Le
premier est un capteur pour écran : c'est une barre placée au dessus ou en
dessous d'un écran et observe les yeux de l'individu en face. Il peut donc
estimer la position du regard sur l'écran.

Pour l'étude dans l'environnement virtuel il faut utiliser un casque de réalité
virtuelle spécial avec des capteurs infrarouges intégrés. Ils premettraient
alors de suivre le regard dans environnement 3D. Donc notre étude, on
s'intéresse à suivre le regard sur un écran, donc ces positions 3D sont
traduites en des positions 2D sur l'écran virtuel.

## Slide 6

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

## Slide 7

Pour cela, la seconde solution seraient des représentations par cartes. On
pourrait par exemple représenter les positions du regard sur une capture de
l'écran. On peut ainsi proprement suivre le regard sur le contenu original assez
facilement. Cette représentation nous donne une idée assez claire du chemin du
regard de l'individu.

## Slide 8

On pourrait également réaliser des heatmaps, ou cartes de chaleurs. Elles
permettent d'indiquer les régions les plus visitées par le regard, et ainsi
distinguer les régions les plus attirantes. Comme sur cet exemple, on peut
très visiblement différencier les zones sur lesquel le regard s'est concentré
(en rouge) des régions qui les sont moins (en bleu). Il existe plein d'autres
formats de représentations des données qui pourraient aider à analyser le
regard, mais dans le cadre de ce travail je me suis contenté de se concentrer
sur ces deux spécialement.

## Slide 9
