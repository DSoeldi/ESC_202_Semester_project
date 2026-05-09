# ESC_202_Semester_project
Google Docs: https://docs.google.com/document/d/1POh07QEm5y5eyBowOd3Yyox-G9CZ4kUh3U6GJYQ0rNg/edit?tab=t.0

## Präsi
https://docs.google.com/presentation/d/16nem0CTda3dVc0Bdxeo9FqWHFYiAJLjosEe6t8yHliA/edit?slide=id.p#slide=id.p

- motivation: Auf lustig, 

- Methode:
    - Diego human teil
    - Raphi zombie
    - Anais: partition knn
    - Zeigen mit beispiele

    - Tests gemacht für alle funktionen

- Analytics:
    - Pop dynamics, was kann man sonsr noch

- Probleme encountered, 
    - Knn problems, 


## @raphi
- to do: . kill radius, do after knn anais
- diego schreiben wenn kill radius fertig
- write tests for my functions thinks about some stuff, edge cases... etc. / make a fly e.g zombie walk. do the functions that are there. for just on test function one test, not multiple.

- in zombie walk.raisewarnung. not raise error lib. math next_after gives really small, distance wird zu next after
- also use in params dictionary. the speed zombie have when they are random walking. do not use get_speed 

## @anais

## @diego
- min heap oder max heap? jenachdem muss flocking geändert werden da dort im heap gesliced wird.
- zombies can go silent/dead/decease if they dont eat humans for some time
- change.velocity bruche statt self.velocity = ...


## future?
- delete dead entities from entity list? How?? That for loops that use entity list do not end up skipping other entities?
- add a mode "dead" for entity class, for Zombies, that have died (their last meal is too long ago)
- ignore dead zombies in prio queue!


