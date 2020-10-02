# repo_for_week4_exercise
The base/template repository for Week 4 Exercise

## Exercise 1

### Part 1

The PhotoObj Table left joined with the SpecObj table (joined on objid and bestobjid respectively), grabbing the columns objid, ra, dec, u, g, r, i, z from PhotoObj, and z and class from SpecObj

    SELECT
       p.objid,p.ra,p.dec,p.u,p.g,p.r,p.i,p.z,
       s.class, s.z as redshift

    FROM PhotoObj AS p
       LEFT JOIN SpecObj AS s ON s.bestobjid = p.objid

    WHERE 
       p.dec BETWEEN 29.75 AND 30
       AND p.ra BETWEEN 180.75 AND 181

[The Results](query_part_1.csv)

### Part 2

the tmassxsc Table left joined with the PhotoObj table (joined on objid from both tables), grabbing the columns ra, dec, J_M_K20FE, H_M_K20FE, K_M_K20FE from tmassxsc, and objid, ra, dec, u, g, r, i, z from PhotoObj


    SELECT TOP 10
       p.objid, p.ra, p.dec, p.u, p.g, p.r, p.i, p.z,
       t.tmassxsc_ra, t.tmassxsc_dec, t.J_M_K20FE, t.H_M_K20FE, t.K_M_K20FE

    FROM TwoMassXSC AS t
       LEFT JOIN PhotoObj AS p ON p.objid = t.objid

    WHERE 
       p.dec BETWEEN 29.75 AND 30
       AND p.ra BETWEEN 180.75 AND 181

[The Results](query_part_2.csv)

### Part 3

the FIRST Table left joined with the PhotoObj table (joined on the objid from both tables) grabbing the columns ra, dec, and integr from FIRST, and objid, ra, dec, u, g, r, i, z from PhotoObj

    SELECT
       p.objid,p.ra,p.dec,p.u,p.g,p.r,p.i,p.z,
       f.ra AS first_ra,f.dec AS first_dec,f.integr

    FROM FIRST AS f
       LEFT JOIN PhotoObj AS p ON p.objid = f.objid

    WHERE
       p.dec BETWEEN 29.75 AND 30
       AND p.ra BETWEEN 180.75 AND 181

[The Results](query_part_3.csv)

Note that there is a huge difference between using PhotoPbj versus FIRST in `WHERE`.