# Race

Race is an app that read a race log and calculate race result.

## Requirements

Python 3

## Execution

```python
git clone https://github.com/vinicius834/race.git

cd race

virtualenv --python=python3 venv

source venv/bin/activate

pyhton app.py
```

```bash
#LOG EXAMPLE 

Hora                               Piloto             Nº Volta   Tempo Volta       Velocidade média da volta
23:49:08.277      038 – F.MASSA                           1		1:02.852                        44,275
23:49:10.858      033 – R.BARRICHELLO                     1		1:04.352                        43,243
23:49:11.075      002 – K.RAIKKONEN                       1		1:04.108                        43,408
23:49:12.667      023 – M.WEBBER                          1		1:04.414                        43,202
23:49:30.976      015 – F.ALONSO                          1		1:18.456                        35,47
23:50:11.447      038 – F.MASSA                           2		1:03.170                        44,053
23:50:14.860      033 – R.BARRICHELLO                     2		1:04.002                        43,48
23:50:15.057      002 – K.RAIKKONEN                       2		1:03.982                        43,493
23:50:17.472      023 – M.WEBBER                          2		1:04.805                        42,941
23:50:37.987      015 – F.ALONSO                          2		1:07.011                        41,528
23:51:14.216      038 – F.MASSA                           3		1:02.769                        44,334
23:51:18.576      033 – R.BARRICHELLO                     3		1:03.716                        43,675
23:51:19.044      002 – K.RAIKKONEN                       3		1:03.987                        43,49
23:51:21.759      023 – M.WEBBER                          3		1:04.287                        43,287
23:51:46.691      015 – F.ALONSO                          3		1:08.704                        40,504
23:52:01.796      011 – S.VETTEL                          1		3:31.31                         13,169
23:52:17.003      038 – F.MASS                            4		1:02.787                        44,321
23:52:22.586      033 – R.BARRICHELLO                     4		1:04.010                        43,474
23:52:22.120      002 – K.RAIKKONEN                       4		1:03.076                        44,118
23:52:25.975      023 – M.WEBBER                          4		1:04.216                        43,335
23:53:06.741      015 – F.ALONSO                          4		1:20.050                        34,763
23:53:39.660      011 – S.VETTEL                          2		1:37.864                        28,435
23:54:57.757      011 – S.VETTEL                          3		1:18.097                        35,633



#RESULT
   
Final Position       Pilot Cod            Pilot Name       Completed Laps     Total Race Time    Best Lap           Average Speed
1°                   038                  F.MASS           4                  0:04:11.578000     00:01:02.769000    44.246             +(0:00:00)
2°                   002                  K.RAIKKONEN      4                  0:04:15.153000     00:01:03.076000    43.627             +(0:00:03.575000)
3°                   033                  R.BARRICHELLO    4                  0:04:16.080000     00:01:03.716000    43.468             +(0:00:04.502000)
4°                   023                  M.WEBBER         4                  0:04:17.722000     00:01:04.216000    43.191             +(0:00:06.144000)
5°                   015                  F.ALONSO         4                  0:04:54.221000     00:01:07.011000    38.066             +(0:00:42.643000)
6°                   011                  S.VETTEL         3                  0:06:27.276000     00:01:18.097000    25.746             +(0:02:15.698000)

Best Race Lap: 00:01:02.769000

```
