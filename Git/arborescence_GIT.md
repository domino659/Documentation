## Arborescence repo GIT

### Branches Permanente

#### Branche main
La version actuelle de l'application, marquée d'un numéro de version tel que V01, V02.
Les modifications du code qui ont été approuvées sur la branche de développement sont publiées périodiquement en tant que versions mineures, ce qui donne un numéro tel que v2.3, v3.1, etc. Les versions majeures sont beaucoup moins fréquentes.

#### Branche dev
Environnement de test du code qui sera publié lors de la prochaine poussée vers la branche principale. Ces versions ajoutent un numéro de version mineur à l'étiquette de la branche principale, à moins que des changements importants ou de rupture ne soient fusionnés. 

### Branches Temporaire

#### Branche de fonctionnalité
Le développement est effectué dans des branches de fonctionnalités individuelles. Chaque branche introduisent une nouvelle fonctionnalité ou un nouveau processus dans l'application. Elles sont toujours créées à partir de la branche main, de sorte qu'elles partaient toutes de l'état actuel de la version de l'application. Une fois complété elles sont mises en file d'attente jusqu'a la review et leurs intégration dans la branche dev.


    main V1.1 dev   fonctionnalité
      ├────────│
      │        ├────────│
      │        ├────│   │
      |        │    │   │
      |        ├────│   │
      │        │        │
      │        ├────────│
      │        │
      ├────────│
      │
      │ V1.2
      │
      ├────────│
      │        ├────────│
