cur_frm.cscript.before_insert = function(frm){
    if(cur_frm.doc.voucher_type == "Expense Claim"){
        cur_frm.doc.account == "Durian - K"
        cur_frm.refresh_field("account")
    }
}