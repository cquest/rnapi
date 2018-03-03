create extension pg_trgm;

create table if not exists rna (id text,id_ex text,siret text,rup_mi text,gestion text,date_creat text,date_decla text,date_publi text,date_disso text,nature text,groupement text,titre text,titre_court text,objet text,objet_social1 text,objet_social2 text,adrs_complement text,adrs_numvoie text,adrs_repetition text,adrs_typevoie text,adrs_libvoie text,adrs_distrib text,adrs_codeinsee text,adrs_codepostal text,adrs_libcommune text,adrg_declarant text,adrg_complemid text,adrg_complemgeo text,adrg_libvoie text,adrg_distrib text,adrg_codepostal text,adrg_achemine text,adrg_pays text,dir_civilite text,telephone text,siteweb text,email text,publiweb text,observation text,position text,maj_time text);

create table if not existsrna_import (id text,id_ex text,siret text,gestion text,date_creat text,date_publi text,nature text,groupement text,titre text,objet text,objet_social1 text,objet_social2 text,adr1 text,adr2 text,adr3 text,adrs_codepostal text,libcom text,adrs_codeinsee text,dir_civilite text,telephone text,siteweb text,email text,observation text,position text,rup_mi text,maj_time text);

BEGIN TRANSACTION;
delete from rna where id like 'W%';
copy rna from "~/data/spd/rna/rna_waldec_out.csv" with (format csv, header true)

truncate rna_import;
copy rna_import from "~/data/spd/rna/rna_import_out.csv" with (format csv, header true)

delete from rna where id not like 'W%';
insert into rna select id,id_ex,siret,rup_mi,gestion,date_creat,null as date_decla, date_publi,null as date_disso,nature,groupement,titre,null as titre_court,objet,objet_social1,objet_social2,adr2 as adrs_complement, null as adrs_numvoie, null as adrs_repetition, null as adrs_typevoie, adr1 as adrs_libvoie, adr3 as adrs_distrib, adrs_codeinsee, adrs_codepostal,libcom as adrs_libcommune,null as adrg_declarant, null as adrg_complemid, null as adrg_complemgeo, null as adrg_libvoie, null as adrg_distrib, null as adrg_codepostal, null as adrg_achemine, null as adrg_pays, dir_civilite,telephone,siteweb,email,null as publiweb, observation,position,maj_time from rna_import;
END TRANSACTION;
