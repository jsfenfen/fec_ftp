from django.db import models



# these are the fec's models; only change is a cycle is added, and file source for the contribs


# populated from fec's candidate master
# http://www.fec.gov/finance/disclosure/metadata/DataDictionaryCandidateMaster.shtml

class Candidate(models.Model):
    cycle = models.PositiveIntegerField()
    cand_id = models.CharField(max_length=9, blank=True)
    cand_name = models.CharField(max_length=200,blank=True, null=True) 
    cand_pty_affiliation = models.CharField(max_length=3, blank=True, null=True)
    cand_election_year = models.PositiveIntegerField(blank=True)
    cand_office_st = models.CharField(max_length=2, blank=True, null=True, help_text="US for president")
    cand_office = models.CharField(max_length=1, null=True,
                              choices=(('H', 'House'), ('S', 'Senate'), ('P', 'President'))
                              )
    cand_office_district = models.CharField(max_length=2, blank=True, null=True, help_text="'00' for at-large congress, senate, president")                          
    cand_ici = models.CharField(max_length=1, null=True,
                                  choices=(('C', 'CHALLENGER'), ('I', 'INCUMBENT'), ('O', 'OPEN SEAT'))
                                   )
    cand_status = models.CharField(max_length=1, null=True,
                                        choices=(('C', 'STATUTORY CANDIDATE'), ('F', 'STATUTORY CANDIDATE FOR FUTURE ELECTION'), ('N', 'NOT YET A STATUTORY CANDIDATE'), ('P', 'STATUTORY CANDIDATE IN PRIOR CYCLE'))
                                         )
    cand_pcc = models.CharField(max_length=9, blank=True, null=True)
    cand_st1 = models.CharField(max_length=34, blank=True, null=True)
    cand_st2 = models.CharField(max_length=34, blank=True, null=True)
    cand_city = models.CharField(max_length=30, blank=True, null=True)
    cand_st = models.CharField(max_length=2, blank=True, null=True)
    cand_zip = models.CharField(max_length=9, blank=True, null=True)


    def __unicode__(self):
        if self.cand_office == 'S':
            return '%s (Senate) %s %s %s' % (self.cand_name, self.cand_office_st, self.cand_pty_affiliation,  self.cand_election_year)
        elif self.cand_office == 'H':
            return '%s %s (House) %s %s %s' % (self.cand_name, self.cand_office_st, self.cand_pty_affiliation,  self.cand_office_district, self.cand_election_year)
        else:
            return self.cand_name
        
# http://www.fec.gov/finance/disclosure/metadata/DataDictionaryCommitteeMaster.shtml
# Populated from fec's committee master            
class Committee(models.Model):
    cycle = models.PositiveIntegerField()
    cmte_id = models.CharField(max_length=9)
    cmte_name = models.CharField(max_length=200, null=True) # amazingly the name is sometimes missing
    tres_nm = models.CharField(max_length=90, blank=True, null=True)
    cmte_st1 = models.CharField(max_length=34, blank=True, null=True)
    cmte_st2 = models.CharField(max_length=34, blank=True, null=True)
    cmte_city = models.CharField(max_length=30, blank=True, null=True)
    cmte_st = models.CharField(max_length=2, blank=True, null=True)
    cmte_zip = models.CharField(max_length=9, blank=True, null=True)
    cmte_dsgn = models.CharField(max_length=1,
                           blank=False,
                           null=True,
                           choices=[('A', 'Authorized by Candidate'),
                                    ('J', 'Joint Fund Raiser'),
                                    ('P', 'Principal Committee of Candidate'),
                                    ('U', 'Unauthorized'),
                                    ('B', 'Lobbyist/Registrant PAC'),
                                    ('D', 'Leadership PAC')])



    cmte_tp = models.CharField(max_length=1,
                              blank=False,
                              null=True,
                              # V, W are Carey committees
                              choices=[('C', 'Communication Cost'),
                                       ('D', 'Delegate'),
                                       ('E', 'Electioneering Communication'),
                                       ('H', 'House'),
                                       ('I', 'Independent Expenditure (Not a Committee'),
                                       ('N', 'Non-Party, Non-Qualified'),
                                       ('O', 'Super PAC'),
                                       ('P', 'Presidential'),
                                       ('Q', 'Qualified, Non-Party'),
                                       ('S', 'Senate'),
                                       ('U', 'Single candidate independent expenditure'),
                                       ('V', 'PAC with Non-Contribution Account - Nonqualified'),
                                       ('W', 'PAC with Non-Contribution Account - Qualified'),
                                       ('X', 'Non-Qualified Party'),
                                       ('Y', 'Qualified Party'),
                                       ('Z', 'National Party Organization') ])
    cmte_pty_affiliation = models.CharField(max_length=3, blank=True, null=True)
    cmte_filing_freq = models.CharField(max_length=1,  null=True,
        choices=[('A', 'ADMINISTRATIVELY TERMINATED'),
                 ('D', 'DEBT'),
                 ('M', 'MONTHLY FILER'),
                 ('Q', 'QUARTERLY FILER'),
                 ('T', 'TERMINATED'),
                 ('W', 'WAIVED')
                 ])

    org_tp= models.CharField(max_length=1, null=True, choices=[
                    ('C', 'CORPORATION'),
                    ('L', 'LABOR ORGANIZATION'),
                    ('M', 'MEMBERSHIP ORGANIZATION'),
                    ('T', 'TRADE ASSOCIATION'),
                    ('V', 'COOPERATIVE'),
                    ('W', 'CORPORATION WITHOUT CAPITAL STOCK')
                  ])
    connected_org_nm=models.CharField(max_length=200, blank=True,  null=True)
    cand_id = models.CharField(max_length=9, blank=True, null=True)


# Description
# http://www.fec.gov/finance/disclosure/metadata/DataDictionaryCandCmteLinkage.shtml
# file is: ftp://ftp.fec.gov/FEC/2012/ccl12.zip

# Candidate committee linkage

class CandComLink(models.Model):
    cycle = models.PositiveIntegerField()
    cand_id = models.CharField(max_length=9, null=True)
    cand_election_yr = models.PositiveIntegerField(null=True)
    fec_election_yr= models.PositiveIntegerField(null=True)
    cmte_id = models.CharField(max_length=9, null=True)
    cmte_tp = models.CharField(max_length=1,
                             blank=False,
                             null=True,
                             # V, W are Carey committees
                             choices=[('C', 'Communication Cost'),
                                      ('D', 'Delegate'),
                                      ('E', 'Electioneering Communication'),
                                      ('H', 'House'),
                                      ('I', 'Independent Expenditure (Not a Committee'),
                                      ('N', 'Non-Party, Non-Qualified'),
                                      ('O', 'Super PAC'),
                                      ('P', 'Presidential'),
                                      ('Q', 'Qualified, Non-Party'),
                                      ('S', 'Senate'),
                                      ('U', 'Single candidate independent expenditure'),
                                      ('V', 'PAC with Non-Contribution Account - Nonqualified'),
                                      ('W', 'PAC with Non-Contribution Account - Qualified'),
                                      ('X', 'Non-Qualified Party'),
                                      ('Y', 'Qualified Party'),
                                      ('Z', 'National Party Organization') ])
    cmte_dsgn = models.CharField(max_length=1,
                                 blank=False,
                                 null=True,
                                 choices=[
                                        ('A', 'Authorized by Candidate'),
                                        ('B', 'Lobbyist/Registrant PAC'),
                                        ('D', 'Leadership PAC'),
                                        ('J', 'Joint Fund Raiser'),
                                        ('P', 'Principal Committee of Candidate'),
                                        ('U', 'Unauthorized')
                                        ])

    linkage_id= models.PositiveIntegerField()
    
# oth: http://www.fec.gov/finance/disclosure/metadata/DataDictionaryCommitteetoCommittee.shtml
# pas2: http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionstoCandidates.shtml
# indiv: http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml


# This contains entries from the OTH, PAS2 and INDIV datasets with two additions: filesource is the name of the file they are from and cycle is the 4-digit cycle represented. 
class contribs(models.Model):
    filesource = models.CharField(max_length=5)
    cycle = models.PositiveIntegerField()
    cmte_id = models.CharField(max_length=9, null=True)
    amndt_ind = models.CharField(max_length=1,
                                 blank=False,
                                 null=True,
                                 choices=[
                                        ('A', 'Amended'),
                                        ('N', 'New'),
                                        ('T', 'Termination'),                                        
                                        ])
    rpt_tp = models.CharField(max_length=3, null=True)
    transaction_pgi = models.CharField(max_length=9, null=True, help_text="EYYYY - E for election type, YYYY for election year")
    image_num = models.CharField(max_length=20, null=True)
    transaction_tp = models.CharField(max_length=9, null=True, help_text="transaction type")
    entity_tp = models.CharField(max_length=3,
                                 blank=False,
                                 null=True,
                                 choices=[
                                        ('CAN', 'Candidate'),
                                        ('CCM', 'Candidate Committee'),
                                        ('COM', 'Committee'),     
                                        ('IND', 'Individual'),
                                        ('ORG', 'Organization-not party or person'),
                                        ('PAC', 'PAC'),
                                        ('PTY', 'Party organization'),                                                                                                                   
                                        ])
    name = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=2, null=True)
    zip_code = models.CharField(max_length=9, null=True)
    employer = models.CharField(max_length=38, null=True)
    occupation = models.CharField(max_length=38, null=True)
    transaction_dt = models.CharField(max_length=8, null=True)
    transaction_amt = models.DecimalField(max_digits=14, decimal_places=2)
    other_id = models.CharField(max_length=9, null=True)
    # is null for some:
    cand_id = models.CharField(max_length=9, null=True)
    tran_id = models.CharField(max_length=32, null=True)
    file_num = models.BigIntegerField(null=True)
    memo_cd = models.CharField(max_length=1, null=True)
    memo_text = models.CharField(max_length=100, null=True)
    sub_id = models.BigIntegerField(null=True)
    
class oppexp(models.Model):
    cycle = models.PositiveIntegerField()
    cmte_id = models.CharField(max_length=9, null=True)
    amndt_ind = models.CharField(max_length=1,
                                 blank=False,
                                 null=True,
                                 choices=[
                                        ('A', 'Amended'),
                                        ('N', 'New'),
                                        ('T', 'Termination'),                                        
                                        ])
    rpt_yr = models.IntegerField(null=True)
    rpt_tp = models.CharField(max_length=3, null=True)
    image_num = models.CharField(max_length=20, null=True)
    line_num = models.CharField(max_length=10, null=True)
    form_tp_cd = models.CharField(max_length=8, null=True)
    sched_tp_cd = models.CharField(max_length=8, null=True)
    name = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=2, null=True)
    zip_code = models.CharField(max_length=9, null=True)
    transaction_dt = models.CharField(max_length=12, null=True)
    transaction_amt = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    transaction_pgi = models.CharField(max_length=9, null=True, help_text="EYYYY - E for election type, YYYY for election year")
    purpose = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=3, null=True, help_text="http://www.fec.gov/finance/disclosure/metadata/CategoryCodes.shtml")
    category_desc = models.CharField(max_length=40, null=True)
    memo_cd = models.CharField(max_length=1, null=True)
    memo_text = models.CharField(max_length=100, null=True)
    entity_tp = models.CharField(max_length=3,
                                 blank=False,
                                 null=True,
                                 choices=[
                                        ('CAN', 'Candidate'),
                                        ('CCM', 'Candidate Committee'),
                                        ('COM', 'Committee'),     
                                        ('IND', 'Individual'),
                                        ('ORG', 'Organization-not party or person'),
                                        ('PAC', 'PAC'),
                                        ('PTY', 'Party organization'),                                                                                                                   
                                        ])
    sub_id = models.BigIntegerField(null=True)
    file_num = models.BigIntegerField(null=True)
    tran_id = models.CharField(max_length=32, null=True)
    back_ref_tran_id = models.CharField(max_length=32, null=True, help_text="back ref transaction id")
    dummy = models.CharField(max_length=1, null=True)



### 
# field names taken directly from metadata, except where noted http://www.fec.gov/finance/disclosure/metadata/metadataforcommitteesummary.shtml
# date fields are imported as they appear, but parsed into coverage_from_date and coverage_through_date. 
## Model reordered to put ids, dates at the top. 
class WebK(models.Model):
    cycle = models.CharField(max_length=4, blank=True, null=True)
    can_id = models.CharField(max_length=9, blank=True, null=True, help_text="FEC-assigned committee id")
    com_id = models.CharField(max_length=9, blank=True, null=True, help_text="FEC-assigned committee id")
    com_nam = models.CharField(max_length=200, blank=True, null=True)

    #### not in original:
    coverage_from_date = models.DateField(null=True)
    coverage_through_date = models.DateField(null=True)
    ####

    cov_sta_dat = models.CharField(max_length=200, blank=True, help_text="Coverage Start Date")
    cov_end_dat = models.CharField(max_length=200, blank=True, help_text="Coverage End Date")
    # Not imported--this can be constructed from the committee id
    lin_ima = models.CharField(max_length=127, blank=True, help_text="Coverage End Date")
    rep_typ = models.CharField(max_length=200, blank=True, null=True)
    com_typ = models.CharField(max_length=1, blank=True, null=True, help_text="committee type")
    com_des = models.CharField(max_length=1, blank=True, null=True, help_text="committee designation")
    fil_fre = models.CharField(max_length=1, blank=True, null=True, help_text="filing frequency")
    add = models.CharField(max_length=255, blank=True, null=True, help_text="address")
    cit = models.CharField(max_length=255, blank=True, null=True, help_text="city")
    sta = models.CharField(max_length=2, blank=True, null=True, help_text="state")
    zip = models.CharField(max_length=9, blank=True, null=True, help_text="zip")
    tre_nam = models.CharField(max_length=200, blank=True, null=True, help_text="treasurers name")
    fec_ele_yea = models.IntegerField(blank=True, null=True, help_text="FEC election year -- integer")
    ind_ite_con = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Individual Itemized Contribution")
    ind_uni_con = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Individual Unitemized Contribution")
    ind_con = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Total contributions from individuals ")
    ind_ref = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="contribution refunds made to individuals ")
    par_com_con = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="contributions from party committees ")
    oth_com_con = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="contributions from other committees ")
    oth_com_ref = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="contribution refunds made to other committees")
    can_con = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Contributions from the candidate ")
    tot_con = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Sum of contributions from all sources ")
    tot_con_ref = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Sum of contribution refunds made to all sources ")
    can_loa = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Sum of loans from the candidate ")
    can_loa_rep = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text=" Candidate Loan Repayment")
    oth_loa = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Sum of loans from other sources ") 
    oth_loa_rep = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Loan repayments to other sources ") 
    tot_loa = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text=" Sum of all loans") 
    tot_loa_rep = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Sum of all loan repayments ") 
    tra_fro_oth_aut_com = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Transfers received from other affiliated or authorized committees * ") 
    tra_fro_non_fed_acc = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Transfer from non Federal Account: Funds outside federal restrictions used for activities that include state or local candidates") 
    tra_fro_non_fed_lev_acc = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Transfer from non Federal Levin Account: special nonfederal funds for specific activities of state or local party committees ") 
    tot_non_fed_tra = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Total non Federal Transfer") 
    oth_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Other Receipt") 
    tot_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Total Receipt") 
    tot_fed_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text=" Total Federal Receipt") 
    ope_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Operating Expenditure") 
    sha_fed_ope_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Shared Federal Operating Expenditure") 
    sha_non_fed_ope_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Shared non Federal Operating Expenditure") 
    tot_ope_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Total Operating Expenditure") 
    off_to_ope_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Offsets to Operating Expenditure") 
    fed_sha_of_joi_act = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Federal Share of Joint Federal Election Activity") 
    non_fed_sha_of_joi_act = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Non Federal Share of Joint Federal Election Activity") 
    non_all_fed_ele_act_par = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Non Allocated Federal Election Activity (Party only)") 
    tot_fed_ele_act = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="   Total Federal Election Activity") 
    fed_can_com_con = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Federal Candidate Committee Contribution: contributions to federal campaigns or other federal committees (e.g. PACs or parties) ") 
    fed_can_con_ref = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Federal Candidate Contribution Refund") 
    ind_exp_mad = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Independent Expenditures Made") 
    coo_exp_par = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Coordinated Expenditure (Party only)") 
    loa_mad = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Loan Made") 
    loa_rep_rec = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Loan Repayments Received") 
    tra_to_oth_aut_com = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Transfer to Other Authorized Committee") 
    fun_dis = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Fundraising Disbursement") 
    off_to_fun_exp_pre = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Offsets to Fundraising Expenses (Presidential only)") 
    exe_leg_acc_dis_pre = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Exempt Legal/Accounting Disbursement (Presidential only)") 
    off_to_leg_acc_exp_pre = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Offsets to Legal/Accounting Expenses (Presidential only)") 
    tot_off_to_ope_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Total Offsets to Operating Expenditure")
    oth_dis = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Other Disbursemen")
    tot_fed_dis = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Total Federal Disbursement")
    tot_dis = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Total Disbursement")
    net_con = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text=" Net Contribution")
    net_ope_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Net Operating Expenditure")
    cas_on_han_beg_of_per = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Cash on Hand Beginning of Period")
    cas_on_han_clo_of_per = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Cash on Hand Closing of Period")
    deb_owe_by_com = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Debt Owed by Committee")
    deb_owe_to_com = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Debt Owed to Committee")
    pol_par_com_ref = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Political Party Committee Refund")

    cas_on_han_beg_of_yea = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Cash on Hand Beginning of Year")
    cas_on_han_clo_of_yea = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Cash on Hand Closing of Year")
    exp_sub_to_lim_pri_yea_pre = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Expenditures Subject to Limit - Prior Year (Presidential only)")
    exp_sub_lim = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Expenditures Subject to Limit")
    fed_fun = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Federal Funds")

    ite_con_exp_con_com = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Itemized Convention Expenditure (Convention Committee only)")
    ite_oth_dis = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Itemized Other Disbursement")
    ite_oth_inc = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Itemized Other Income")
    ite_oth_ref_or_reb = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Itemized Other Refunds or Rebates")
    ite_ref_or_reb = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Itemized Refunds or Rebates")
    oth_fed_ope_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Other Federal Operating Expenditures")
    sub_con_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Subtotal Convention Expenses")
    sub_oth_ref_or_reb = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Subtotal Other Refunds or Rebates")
    sub_ref_or_reb = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Subtotal Refunds or Rebates")
    tot_com_cos = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Total Communication Cost")
    tot_exp_sub_to_lim_pre = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Total Expenditures Subject to Limit (Presidential only)")
    uni_con_exp = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Unitemized Convention Expenses")
    uni_oth_dis = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Unitemized Other Disbursements")
    uni_oth_inc = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text=" Unitemized Other Income")
    uni_oth_ref_or_reb = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Unitemized other Refunds or Rebates")
    uni_ref_or_reb = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Unitemized Refunds or Rebates")
    org_tp = models.CharField(max_length=1, null=True, help_text="Organization Type")
    
    create_time = models.DateTimeField(auto_now_add=True, null=True, help_text="This is the time that we created the webk, not the time FEC added it.")



