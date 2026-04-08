# ESC_202_Semester_project
Google Docs: https://docs.google.com/document/d/1POh07QEm5y5eyBowOd3Yyox-G9CZ4kUh3U6GJYQ0rNg/edit?tab=t.0

## classes that were written:
- entity
    - __init__
        - instead of 2 attributes (speed & direction), I made 1 attribute velocity, which is a vector!
        - Should we add a varaiable, which stores the capacity of an entity to keep on running, which is somehow calculated through some function of time/distance & velocity??
    - __functions__:
        - I made 2 function: entity.get_speed() & entity.get_direction(), incase you need them... But is the second fucntion relevant for us???
        - I made a function repr for printing the entity list (to see everything is working as it should)
        - I added functions for changing variables, to be able to check (even after initiation of an instance) that the type one changes to is correct. Use them!!!
            FOR EXAMPLE:
            __instead of: self.direction = new_direction,
            use: self.change_direction(new_direction)__
        - I added functions called validate_... There is one for each "kind" (e.g. pos & velocity can be checked by same fucntion) of attribute, to check they ar evalid inputs. They are always called when an entity is instantiated and when an entity attribute is changed (e.g. enitity1.change_velocity(new_velocity))



## functions that were written:


## @raphi
- I saw that in your Random Walk function for Zombies, there are only 4 possible directions, in which the Zombies, can walk. Is this how we want to do it? We could also use an n.random.uniform(a,b) to generate an infinte possibility of random directions! (- anais)

## @anais

## @diego
