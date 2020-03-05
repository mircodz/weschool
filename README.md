# WeSchool API

Thanks to [.fabris](https://github.com/0fabris) for the research into the WeSchool API.

## Retrieving Information

``` python
s = weschool.Session('...', '...')
s.login()

groups   = s.get_groups()
boards   = s.get_boards(groups['groups'][0]['id'])
elements = s.get_board_elemenst(boards[0]['id'])
```

## Useful Tools
``` python
exercises = s.get_exercises(groups['groups'][0]['id'])
weschool.solve(s, exercises[0]['id'])

weschool.complete_group(s, groups['groups'][0]['id'])
```
