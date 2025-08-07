# 2025H-420-930-MA TP3 : SYSTÈME DE GESTION DE BIBLIOTHÈQUE

**Nom des étudiants :** [Vos noms ici]

Le but de ce TP est de refactoriser un code existant qui gère une bibliothèque.
Le code viole intentionnellement les principes SOLID et manque d'implémentation
correcte du patron Observateur.

## Consignes

1. Cloner ce dépôt.
2. Effectuer le refactoring du code selon la section "Consignes de refactoring"
   ci-dessous.
3. Soumettre votre dépôt refactorisé sur Omnivox selon les instructions de
   l'énoncé disponible sur le site du cours.

### Consignes de refactoring

1. Identifier et corriger les violations des principes SOLID. Elles sont
   identifiées par des commentaires dans le code.
2. Implémenter correctement le patron Observateur pour les notifications.
3. Modulariser le code en plusieurs fichiers appropriés.

### Acronymes SOLID:

- SRP = Single Responsibility Principle
- OCP = Open/Closed Principle
- LSP = Liskov Substitution Principle
- ISP = Interface Segregation Principle
- DIP = Dependency Inversion Principle

## Comment exécuter le code

Vous pouvez exécuter le code en utilisant `uv`:

```bash
uv run main
```