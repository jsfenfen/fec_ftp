copy ftpdata_contribs (filesource, cycle, cmte_id, amndt_ind , rpt_tp , transaction_pgi , image_num, transaction_tp, entity_tp, name, city, state, zip_code, employer, occupation, transaction_dt, transaction_amt, other_id, tran_id, file_num, memo_cd, memo_text, sub_id) from '/Users/jfenton/github-whitelabel/read_FEC/fecreader/ftpdata/data/12/indiv12-fixed.txt' with delimiter as '|' null as '';

