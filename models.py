from django.db import models
import datetime
# Create your models here.
class File_Name_Store(models.Model):
    Date_Upload=models.DateField()	
    File_Name=models.CharField(max_length=300,blank=True,null=True)	
    User_name=models.CharField(max_length=25,blank=True,null=True)

    def __str__(self):
        return self.File_Name

# ------------------NODAL MAIN TABLE -----------------------------

class Transaction_Details_test(models.Model):
    Pg_Ref_Num=models.CharField(max_length=100)
    Payment_Method=models.CharField(max_length=10)
    Mop_Type=models.CharField(max_length=20)
    Order_Id=models.CharField(max_length=50)
    Business_Name=models.CharField(max_length=100)
    Currency=models.FloatField()
    Transaction_Type=models.CharField(max_length=25)
    Transaction_Date=models.DateField(blank=True,null=True)
    Transaction_Region=models.CharField(max_length=25)
    Card_Holder_Type=models.CharField(max_length=30)
    Acquirer=models.CharField(max_length=50)
    Total_Amount=models.FloatField()
    Bank_comission=models.FloatField()
    Ipay_comission=models.FloatField()
    Bank_GST=models.FloatField()
    Ipay_GST=models.FloatField()
    Base_Amount=models.FloatField()
    ACQ_ID=models.CharField(max_length=100)
    RRN=models.CharField(max_length=100)
    Post_Settled_Flag=models.CharField(max_length=25,blank=True)
    Refund_Flag=models.CharField(max_length=25,blank=True)
    Refund_id=models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.Order_Id

class Transaction_Details(models.Model):
    Pg_Ref_Num=models.CharField(max_length=100)
    Payment_Method=models.CharField(max_length=10)
    Mop_Type=models.CharField(max_length=20)
    Order_Id=models.CharField(max_length=50)
    Business_Name=models.CharField(max_length=100)
    Currency=models.FloatField()
    Transaction_Type=models.CharField(max_length=25)
    Transaction_Date=models.DateField(blank=True,null=True)
    Transaction_Region=models.CharField(max_length=25)
    Card_Holder_Type=models.CharField(max_length=30)
    Acquirer=models.CharField(max_length=50)
    Total_Amount=models.FloatField()
    Bank_comission=models.FloatField()
    Ipay_comission=models.FloatField()
    Bank_GST=models.FloatField()
    Ipay_GST=models.FloatField()
    Base_Amount=models.FloatField()
    ACQ_ID=models.CharField(max_length=100)
    RRN=models.CharField(max_length=100)
    Post_Settled_Flag=models.CharField(max_length=25,blank=True)
    Refund_Flag=models.CharField(max_length=25,blank=True)
    Refund_id=models.CharField(max_length=100,blank=True)
    Settle_Date=models.DateField(blank=True,null=True)
    Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Reversal_Date1=models.DateField(blank=True,null=True)
    Reversal_Date2=models.DateField(blank=True,null=True)
    Reversal_Status=models.CharField(max_length=10,blank=True,null=True)
    Reversal_Amount=models.FloatField(blank=True,null=True)
    Reversal1_Amount=models.FloatField(blank=True,null=True)
    File_upload_Date=models.DateTimeField(blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True)
    Db_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Match_Summary_Trans=models.CharField(max_length=10,blank=True,null=True)   

    def __str__(self):
        return self.Pg_Ref_Num

class Mpr_ccdc_Details(models.Model):
    Merchant_Code=models.CharField(max_length=25,blank=True,null=True)
    Terminal_Number=models.CharField(max_length=25,blank=True,null=True)
    Rec_Fmt=models.CharField(max_length=25,blank=True,null=True)
    Bat_Nbr=models.CharField(max_length=15,blank=True,null=True)
    Card_Type=models.CharField(max_length=50,blank=True,null=True)
    Card_Number=models.CharField(max_length=100,blank=True,null=True)
    Trans_Date=models.DateField(blank=True)
    Settle_Date=models.DateField(blank=True)
    Approv_code=models.CharField(max_length=25,blank=True,null=True)
    Intnl_Amount=models.FloatField(blank=True,null=True)
    Domestic_Amount=models.FloatField()
    Tran_Id=models.CharField(max_length=150,blank=True)
    Upvalue=models.CharField(max_length=25,blank=True,null=True)
    Pg_Ref_Num=models.CharField(max_length=25,blank=True)
    Msf=models.FloatField(blank=True,null=True)
    Serv_Tax=models.FloatField(blank=True,null=True)
    Sb_Cess=models.FloatField(blank=True,null=True)
    Kk_Cess=models.FloatField(blank=True,null=True)
    CGST_Amount=models.FloatField(blank=True,null=True)
    SGST_Amount=models.FloatField(blank=True,null=True)
    IGST_Amount=models.FloatField(blank=True,null=True)
    UTGST_Amount=models.FloatField(blank=True,null=True)
    Net_Amount=models.FloatField()
    Debit_Credit_Type=models.CharField(max_length=25,blank=True,null=True)
    UDF1=models.CharField(max_length=25,blank=True,null=True)
    UDF2=models.CharField(max_length=25,blank=True,null=True)
    UDF3=models.CharField(max_length=25,blank=True,null=True)
    UDF4=models.CharField(max_length=25,blank=True,null=True)
    UDF5=models.CharField(max_length=25,blank=True,null=True)
    Sequence_Number=models.CharField(max_length=100,blank=True,null=True)
    ARN_RRN_Number=models.CharField(max_length=100,blank=True,null=True)
    Invoice_Number=models.CharField(max_length=25,blank=True,null=True)
    GSTN_Transaction_Id=models.CharField(max_length=25,blank=True,null=True)
    Bank_Name=models.CharField(max_length=15,blank=True,null=True)
    Nodal_Credit_Date=models.DateField(blank=True,null=True)
    transactiondetails=models.ForeignKey(
        Transaction_Details,null=True, on_delete=models.CASCADE,
        related_name='mprdetails')
    File_upload_Date=models.DateTimeField(blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True)  
    Nodal_Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Remarks=models.CharField(max_length=50,blank=True,null=True)
    Mpr_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    def __str__(self):
         return self.Pg_Ref_Num

# ------------------TEST/TEMP TABLE NODAL ---------------------------
class Autopay_Mpr_temp(models.Model):
    Merchant_Code=models.CharField(max_length=25,blank=True)
    Terminal_Number=models.CharField(max_length=25,blank=True)
    Rec_Fmt=models.CharField(max_length=25,blank=True)
    Bat_Nbr=models.CharField(max_length=15,blank=True)
    Card_Type=models.CharField(max_length=50,blank=True)
    Card_Number=models.CharField(max_length=100,blank=True)
    Trans_Date=models.CharField(max_length=25,blank=True,null=True)
    Settle_Date=models.CharField(max_length=25,blank=True,null=True)
    Approv_code=models.CharField(max_length=25,blank=True,null=True)
    Intnl_Amount=models.CharField(max_length=10,blank=True,null=True)
    Domestic_Amount=models.FloatField()
    Tran_Id=models.CharField(max_length=150,blank=True)
    Upvalue=models.CharField(max_length=25,blank=True)
    Pg_Ref_Num=models.CharField(max_length=25,blank=True)
    Msf=models.CharField(max_length=10,blank=True,null=True)
    Serv_Tax=models.CharField(max_length=10,blank=True,null=True)
    Sb_Cess=models.CharField(max_length=10,blank=True,null=True)
    Kk_Cess=models.CharField(max_length=10,blank=True,null=True)
    CGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    SGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    IGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    UTGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    Net_Amount=models.FloatField()
    Debit_Credit_Type=models.CharField(max_length=25,blank=True)
    UDF1=models.CharField(max_length=25,blank=True,null=True)
    UDF2=models.CharField(max_length=25,blank=True,null=True)
    UDF3=models.CharField(max_length=25,blank=True,null=True)
    UDF4=models.CharField(max_length=25,blank=True,null=True)
    UDF5=models.CharField(max_length=25,blank=True,null=True)
    Sequence_Number=models.CharField(max_length=25,blank=True,null=True)
    ARN_RRN_Number=models.CharField(max_length=50,blank=True,null=True)
    Invoice_Number=models.CharField(max_length=25,blank=True,null=True)
    GSTN_Transaction_Id=models.CharField(max_length=26,blank=True,null=True)

    def __str__(self):
         return self.Pg_Ref_Num

class Bob_mpr_temp(models.Model):
    Merchant_Code=models.CharField(max_length=25,blank=True)
    Terminal_Number=models.CharField(max_length=25,blank=True)
    Rec_Fmt=models.CharField(max_length=25,blank=True)
    Bat_Nbr=models.CharField(max_length=15,blank=True)
    Card_Type=models.CharField(max_length=50,blank=True)
    Card_Number=models.CharField(max_length=100,blank=True)
    Trans_Date=models.CharField(max_length=25,blank=True,null=True)
    Settle_Date=models.CharField(max_length=25,blank=True,null=True)
    Approv_code=models.CharField(max_length=25,blank=True,null=True)
    Intnl_Amount=models.CharField(max_length=10,blank=True,null=True)
    Domestic_Amount=models.FloatField()
    Tran_Id=models.CharField(max_length=25,blank=True)
    Upvalue=models.CharField(max_length=25,blank=True)
    Pg_Ref_Num=models.CharField(max_length=25,blank=True)
    Msf=models.CharField(max_length=10,blank=True,null=True)
    Serv_Tax=models.CharField(max_length=10,blank=True,null=True)
    Sb_Cess=models.CharField(max_length=10,blank=True,null=True)
    Kk_Cess=models.CharField(max_length=10,blank=True,null=True)
    CGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    SGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    IGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    UTGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    Net_Amount=models.FloatField()
    Debit_Credit_Type=models.CharField(max_length=25,blank=True)
    UDF1=models.CharField(max_length=25,blank=True,null=True)
    UDF2=models.CharField(max_length=25,blank=True,null=True)
    UDF3=models.CharField(max_length=25,blank=True,null=True)
    UDF4=models.CharField(max_length=25,blank=True,null=True)
    UDF5=models.CharField(max_length=25,blank=True,null=True)
    Sequence_Number=models.CharField(max_length=25,blank=True,null=True)
    ARN_RRN_Number=models.CharField(max_length=50,blank=True,null=True)
    Invoice_Number=models.CharField(max_length=25,blank=True,null=True)
    GSTN_Transaction_Id=models.CharField(max_length=25,blank=True,null=True)
   
    def __str__(self):
         return self.Pg_Ref_Num

class Icici_Mpr_test(models.Model):
    Merchant_Code=models.CharField(max_length=25,blank=True)
    Terminal_Number=models.CharField(max_length=25,blank=True)
    Rec_Fmt=models.CharField(max_length=25,blank=True)
    Bat_Nbr=models.CharField(max_length=15,blank=True)
    Card_Type=models.CharField(max_length=50,blank=True)
    Card_Number=models.CharField(max_length=100,blank=True)
    Trans_Date=models.CharField(max_length=25,blank=True,null=True)
    Settle_Date=models.CharField(max_length=25,blank=True,null=True)
    Approv_code=models.CharField(max_length=25,blank=True,null=True)
    Intnl_Amount=models.CharField(max_length=10,blank=True,null=True)
    Domestic_Amount=models.FloatField()
    Tran_Id=models.CharField(max_length=25,blank=True)
    Upvalue=models.CharField(max_length=25,blank=True)
    Pg_Ref_Num=models.CharField(max_length=25,blank=True)
    Msf=models.CharField(max_length=10,blank=True,null=True)
    Serv_Tax=models.CharField(max_length=10,blank=True,null=True)
    Sb_Cess=models.CharField(max_length=10,blank=True,null=True)
    Kk_Cess=models.CharField(max_length=10,blank=True,null=True)
    CGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    SGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    IGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    UTGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    Net_Amount=models.FloatField()
    Debit_Credit_Type=models.CharField(max_length=25,blank=True)
    UDF1=models.CharField(max_length=25,blank=True,null=True)
    UDF2=models.CharField(max_length=25,blank=True,null=True)
    UDF3=models.CharField(max_length=25,blank=True,null=True)
    UDF4=models.CharField(max_length=25,blank=True,null=True)
    UDF5=models.CharField(max_length=25,blank=True,null=True)
    Sequence_Number=models.CharField(max_length=25,blank=True,null=True)
    ARN_RRN_Number=models.CharField(max_length=50,blank=True,null=True)
    Invoice_Number=models.CharField(max_length=25,blank=True,null=True)
    GSTN_Transaction_Id=models.CharField(max_length=25,blank=True,null=True)

    def __str__(self):
         return self.Pg_Ref_Num

class payu_dc_Nodal_temp(models.Model):

    External_MID=models.CharField(max_length=25,blank=True,null=True)	
    External_TID=models.CharField(max_length=25,blank=True,null=True)		
    UPI_Merchant_Id=models.CharField(max_length=100,blank=True,null=True)		
    Merchant_Name=models.CharField(max_length=25,blank=True,null=True)		
    Merchant_Vpa=models.CharField(max_length=25,blank=True,null=True)
    Payer_Vpa=models.CharField(max_length=25,blank=True,null=True)
    Payee_Vpa=models.CharField(max_length=25,blank=True,null=True)
    UPI_Trxn_Id=models.CharField(max_length=100,blank=True,null=True)	
    Order_Id=models.CharField(max_length=100,blank=True,null=True)	
    Txn_Ref_No_RRN=models.CharField(max_length=100,blank=True,null=True)	
    Transaction_Req_Date=models.CharField(max_length=25,blank=True,null=True)	
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Currency=models.CharField(max_length=15,blank=True,null=True)	
    Transaction_Amount=models.CharField(max_length=15,blank=True,null=True)
    MSF_Amount=models.CharField(max_length=15,blank=True,null=True)
    CGST_Amount=models.CharField(max_length=15,blank=True,null=True)
    SGST_Amount=models.CharField(max_length=15,blank=True,null=True)
    IGST_Amount=models.CharField(max_length=15,blank=True,null=True)
    UTGST_Amount=models.CharField(max_length=15,blank=True,null=True)
    Net_Amount=models.CharField(max_length=15,blank=True,null=True)	
    Refund_Flag=models.CharField(max_length=25,blank=True,null=True)
    GST_Invoice_No=models.CharField(max_length=25,blank=True,null=True)
    Trans_Type=models.CharField(max_length=25,blank=True,null=True)
    Pay_Type=models.CharField(max_length=25,blank=True,null=True)
    CR_DR=models.CharField(max_length=25,blank=True,null=True)

class payu_dc_Nodal_new_temp(models.Model):
    Merchant_Code=models.CharField(max_length=25,blank=True)
    Terminal_Number=models.CharField(max_length=25,blank=True)
    Rec_Fmt=models.CharField(max_length=25,blank=True)
    Bat_Nbr=models.CharField(max_length=15,blank=True)
    Card_Type=models.CharField(max_length=50,blank=True)
    Card_Number=models.CharField(max_length=25,blank=True)
    Trans_Date=models.CharField(max_length=25,blank=True,null=True)
    Settle_Date=models.CharField(max_length=25,blank=True,null=True)
    Approv_code=models.CharField(max_length=25,blank=True,null=True)
    Intnl_Amount=models.CharField(max_length=10,blank=True,null=True)
    Domestic_Amount=models.FloatField()
    Tran_Id=models.CharField(max_length=25,blank=True)
    Upvalue=models.CharField(max_length=25,blank=True)
    Pg_Ref_Num=models.CharField(max_length=25,blank=True)
    Msf=models.CharField(max_length=10,blank=True,null=True)
    Serv_Tax=models.CharField(max_length=10,blank=True,null=True)
    Sb_Cess=models.CharField(max_length=10,blank=True,null=True)
    Kk_Cess=models.CharField(max_length=10,blank=True,null=True)
    CGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    SGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    IGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    UTGST_Amount=models.CharField(max_length=10,blank=True,null=True)
    Net_Amount=models.FloatField()
    Debit_Credit_Type=models.CharField(max_length=25,blank=True)
    UDF1=models.CharField(max_length=25,blank=True,null=True)
    UDF2=models.CharField(max_length=25,blank=True,null=True)
    UDF3=models.CharField(max_length=25,blank=True,null=True)
    UDF4=models.CharField(max_length=25,blank=True,null=True)
    UDF5=models.CharField(max_length=25,blank=True,null=True)
    Sequence_Number=models.CharField(max_length=100,blank=True,null=True)
    ARN_RRN_Number=models.CharField(max_length=100,blank=True,null=True)
    Invoice_Number=models.CharField(max_length=25,blank=True,null=True)
    GSTN_Transaction_Id=models.CharField(max_length=25,blank=True,null=True)
    

# ----------------------MERCHANT  MAIN TABLE ------------------------------------

class Rail_Ticket_Sale(models.Model):
    Reservation_Id=models.CharField(max_length=50,unique=True)
    Booking_Date=models.DateField()
    Bank_Txn_Number=models.CharField(max_length=50)
    Sale_Amount=models.FloatField(blank=True)
    Bank_id=models.CharField(max_length=10)
    Bank_Name=models.CharField(max_length=25,blank=True)
    Sale_pg_id=models.CharField(max_length=125,blank=True,null=True)
    Actual_Credit_Date=models.DateField(blank=True,null=True)
    Sale_Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Credit_Amount=models.FloatField(blank=True,null=True)
    File_upload_Date=models.DateTimeField(blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True) 
    Db_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Match_Summary_Trans=models.CharField(max_length=10,blank=True,null=True)  
    product_type=models.CharField(max_length=25,blank=True,null=True) 
    mpr_trans_status=models.CharField(max_length=25,blank=True,null=True)
    bank_extra_ref=models.CharField(max_length=50,blank=True,null=True)
    Entity_Code=models.CharField(max_length=10,blank=True,null=True)
    

    def __str__(self):
        return self.Reservation_Id

class Rail_Ticket_Refund(models.Model):

    Reservation_Id=models.CharField(max_length=50)
    Transaction_Date=models.DateField()
    Bank_Txn_Id=models.CharField(max_length=50,blank=True,null=True)
    Bank_Refund_Txn_Id=models.CharField(max_length=50,blank=True,null=True)
    Refund_Amount=models.FloatField(blank=True)
    Refund_Status=models.CharField(max_length=10,blank=True,null=True)
    Bank_Name=models.CharField(max_length=25,blank=True,null=True)
    Actual_Refund_Date=models.DateField(blank=True,null=True)
    Bank_id=models.CharField(max_length=5,blank=True,null=True)
    Cancellation_id=models.CharField(max_length=25,blank=True,null=True)
    Refund_pg_id=models.CharField(max_length=125,blank=True,null=True)
    Actual_Debit_Date=models.DateField(blank=True,null=True)
    Refund_Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Otp_Flag=models.CharField(max_length=10,blank=True,null=True)
    Reversal_Date1=models.DateField(blank=True,null=True)
    Reversal_Date2=models.DateField(blank=True,null=True)
    Reversal_Status=models.CharField(max_length=10,blank=True,null=True)
    Debit_Amount=models.FloatField(blank=True,null=True)
    Reversal_Amount=models.FloatField(blank=True,null=True)
    Reversal1_Amount=models.FloatField(blank=True,null=True)
    File_upload_Date=models.DateTimeField(blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True) 
    Db_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Match_Summary_Trans=models.CharField(max_length=10,blank=True,null=True)  
    product_type=models.CharField(max_length=25,blank=True,null=True) 
    mpr_trans_status=models.CharField(max_length=25,blank=True,null=True)
    bank_extra_ref=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.Reservation_Id

class Ipay_Rail_Mpr(models.Model):

    Merchant_Name=models.CharField(max_length=50,blank=True,null=True)
    MID=models.CharField(max_length=50,blank=True)
    Transaction_Id=models.CharField(max_length=50,blank=True,null=True)
    Order_Id=models.CharField(max_length=50,blank=True,null=True)
    Transaction_Date=models.DateField(blank=True,null=True)
    Settlement_Date=models.DateField()
    Refund_Request_Date=models.DateField(blank=True,null=True)
    Transaction_type=models.CharField(max_length=50,blank=True)
    Gross_Amount=models.FloatField(blank=True,null=True)
    Aggregator_Com=models.FloatField(blank=True,null=True)
    Acquirer_Comm=models.FloatField(blank=True,null=True)
    Payable_Merchant=models.FloatField(blank=True)
    Payout_from_Nodal=models.FloatField(blank=True,null=True)
    BankName_Receive_Funds=models.CharField(max_length=50,blank=True,null=True)
    Nodal_Account_No=models.CharField(max_length=50,blank=True,null=True)
    Aggregator_Name=models.CharField(max_length=50,blank=True,null=True)
    Acquirer_Name=models.CharField(max_length=50,blank=True,null=True)
    Refund_Flag=models.CharField(max_length=10,blank=True,null=True)
    Payments_Type=models.CharField(max_length=50,blank=True,null=True)
    MOP_Type=models.CharField(max_length=50,blank=True,null=True)
    Credit_Debit_Date=models.DateField(blank=True,null=True)
    Bank_Name=models.CharField(max_length=15,blank=True,null=True)
    Refund_Order_Id=models.CharField(max_length=50,blank=True,null=True)
    Railticketsaler=models.ForeignKey(
       Rail_Ticket_Sale,null=True, on_delete=models.CASCADE,
            related_name='railticketsale')
    Railticketrefund=models.ForeignKey(
        Rail_Ticket_Refund,null=True, on_delete=models.CASCADE,
            related_name='railticketrefund')
    Acq_Id=models.CharField(max_length=125,blank=True,null=True)
    Approve_code=models.CharField(max_length=50,blank=True,null=True)
    Arn_No=models.CharField(max_length=150,blank=True,null=True)
    Card_No=models.CharField(max_length=150,blank=True,null=True)
    Tid=models.CharField(max_length=125,blank=True,null=True)
    Remarks=models.CharField(max_length=50,blank=True,null=True)
    Bank_Ref_id=models.CharField(max_length=125,blank=True,null=True)
    File_upload_Date=models.DateTimeField(blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True)
    Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Mpr_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Merchant_code=models.CharField(max_length=50,blank=True,null=True)
    Rec_Fmt=models.CharField(max_length=50,blank=True,null=True)
    Card_type=models.CharField(max_length=100,blank=True,null=True)
    Intl_Amount=models.FloatField(blank=True,null=True)
    Domestic_Amount=models.FloatField(blank=True,null=True)
    UDF1=models.CharField(max_length=300,blank=True,null=True)
    GST_Number=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.Order_Id

# ----------------- MERCHANT TEST/TEMP TABLE ---------------------------

class Rail_Ticket_Sale_test(models.Model):
    Reservation_Id=models.CharField(max_length=50)
    Booking_Date=models.DateField()
    Bank_Txn_Number=models.CharField(max_length=50)
    Sale_Amount=models.FloatField(blank=True)
    Bank_id=models.CharField(max_length=10)
    Bank_Name=models.CharField(max_length=25,blank=True)
    product_type=models.CharField(max_length=25,blank=True,null=True)
    bank_extra_ref=models.CharField(max_length=50,blank=True,null=True)
    Entity_Code=models.CharField(max_length=10,blank=True,null=True)
    
  
class Rail_Ticket_Refund_test(models.Model):

    Reservation_Id=models.CharField(max_length=50)
    Transaction_Date=models.DateField()
    Bank_Txn_Id=models.CharField(max_length=50,blank=True,null=True)
    Bank_Refund_Txn_Id=models.CharField(max_length=50,blank=True,null=True)
    Refund_Amount=models.FloatField(blank=True)
    Refund_Status=models.CharField(max_length=10,blank=True,null=True)
    Bank_Name=models.CharField(max_length=25,blank=True,null=True)
    Actual_Refund_Date=models.CharField(max_length=25,blank=True,null=True)
    Bank_id=models.CharField(max_length=5,blank=True,null=True)
    Cancellation_id=models.CharField(max_length=25,blank=True,null=True)
    Otp_Flag=models.CharField(max_length=10,blank=True,null=True)
    product_type=models.CharField(max_length=25,blank=True,null=True)
    bank_extra_ref=models.CharField(max_length=50,blank=True,null=True)

class Ipay_Rail_Mpr_test(models.Model):

    Sr_No=models.CharField(max_length=25,blank=True,null=True)
    Merchant_Name=models.CharField(max_length=50,blank=True)
    MID=models.CharField(max_length=50,blank=True,null=True)
    Transaction_Id=models.CharField(max_length=50,null=True)
    Order_Id=models.CharField(max_length=50,null=True)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Refund_Request_Date=models.CharField(max_length=25,blank=True,null=True)
    Transaction_type=models.CharField(max_length=20,blank=True,null=True)
    Gross_Amount=models.CharField(max_length=25,blank=True,null=True)
    Aggregator_Com=models.CharField(max_length=25,blank=True,null=True)
    Acquirer_Comm=models.CharField(max_length=25,blank=True,null=True)
    Payable_Merchant=models.CharField(max_length=25,blank=True,null=True)
    Payout_from_Nodal=models.CharField(max_length=25,blank=True,null=True)
    BankName_Receive_Funds=models.CharField(max_length=50,blank=True,null=True)
    Nodal_Account_No=models.CharField(max_length=50,blank=True,null=True)
    Aggregator_Name=models.CharField(max_length=50,blank=True,null=True)
    Acquirer_Name=models.CharField(max_length=50,blank=True,null=True)
    Refund_Flag=models.CharField(max_length=10,blank=True,null=True)
    Payments_Type=models.CharField(max_length=25,blank=True,null=True)
    MOP_Type=models.CharField(max_length=50,blank=True,null=True)
    Refund_Order_Id=models.CharField(max_length=50,blank=True,null=True)
    Acq_Id=models.CharField(max_length=125,blank=True,null=True)
    RRN=models.CharField(max_length=125,blank=True,null=True) 


class Hdfc_Mer_Mpr_temp(models.Model):
    
    Merchant_Code=models.CharField(max_length=25,blank=True)
    Terminal_Number=models.CharField(max_length=25,blank=True)
    Rec_Fmt=models.CharField(max_length=25,blank=True)
    Bat_Nbr=models.CharField(max_length=15,blank=True)
    Card_Type=models.CharField(max_length=50,blank=True)
    Card_Number=models.CharField(max_length=25,blank=True)
    Trans_Date=models.DateField(blank=True,null=True)
    Settle_Date=models.DateField(blank=True,null=True)
    Approv_code=models.CharField(max_length=25,blank=True)
    Intnl_Amount=models.FloatField(blank=True,null=True)
    Domestic_Amount=models.FloatField(blank=True,null=True)
    Tran_Id=models.CharField(max_length=25,blank=True,null=True)
    Upvalue=models.CharField(max_length=25,blank=True)
    Order_id=models.CharField(max_length=25,blank=True)
    Msf=models.CharField(max_length=25,blank=True,null=True)
    Serv_Tax=models.CharField(max_length=25,blank=True,null=True)
    Sb_Cess=models.CharField(max_length=25,blank=True,null=True)
    Kk_Cess=models.CharField(max_length=25,blank=True,null=True)
    CGST_Amount=models.CharField(max_length=25,blank=True,null=True)
    SGST_Amount=models.CharField(max_length=25,blank=True,null=True)
    IGST_Amount=models.CharField(max_length=25,blank=True,null=True)
    UTGST_Amount=models.CharField(max_length=25,blank=True,null=True)
    Net_Amount=models.FloatField(blank=True,null=True)
    Debit_Credit_Type=models.CharField(max_length=25,blank=True)
    UDF1=models.CharField(max_length=25,blank=True,null=True)
    UDF2=models.CharField(max_length=25,blank=True,null=True)
    UDF3=models.CharField(max_length=25,blank=True,null=True)
    UDF4=models.CharField(max_length=25,blank=True,null=True)
    UDF5=models.CharField(max_length=25,blank=True,null=True)
    Sequence_Number=models.CharField(max_length=25,blank=True,null=True)
    ARN_RRN_Number=models.CharField(max_length=50,blank=True,null=True)
    Invoice_Number=models.CharField(max_length=25,blank=True,null=True)
    GSTN_Transaction_Id=models.CharField(max_length=25,blank=True,null=True)

class hdfc_mermpr_sale_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Approve_Code=models.CharField(max_length=150,blank=True)
    Order_Id=models.CharField(max_length=50)
    Transaction_Id=models.CharField(max_length=50)
    Payable_Merchant=models.FloatField(blank=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Arn_No=models.CharField(max_length=150,blank=True)
    Card_No=models.CharField(max_length=125,blank=True)
    MID=models.CharField(max_length=10,blank=True)
    Tid=models.CharField(max_length=50,blank=True)
    Remarks=models.CharField(max_length=25,blank=True)

    
class hdfc_mermpr_refund_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Approve_Code=models.CharField(max_length=150,blank=True)
    Order_Id=models.CharField(max_length=50)
    Transaction_Id=models.CharField(max_length=50)
    Bank_Ref_Id=models.CharField(max_length=50)
    Payable_Merchant=models.FloatField(blank=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Arn_No=models.CharField(max_length=150,blank=True)
    Card_No=models.CharField(max_length=125,blank=True)
    MID=models.CharField(max_length=10,blank=True)
    Tid=models.CharField(max_length=50,blank=True)
    Remarks=models.CharField(max_length=25,blank=True)
    Refund_Type=models.CharField(max_length=15,blank=True)

class hdfc_mermpr_sale_excel_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Approve_Code=models.CharField(max_length=10,blank=True)
    Order_Id=models.CharField(max_length=50)
    Transaction_Id=models.CharField(max_length=50)
    Payable_Merchant=models.FloatField(blank=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Arn_No=models.CharField(max_length=50,blank=True)
    Card_No=models.CharField(max_length=25,blank=True)
    MID=models.CharField(max_length=10,blank=True)
    Tid=models.CharField(max_length=15,blank=True)
    Remarks=models.CharField(max_length=250,blank=True)
    Sequence_Number=models.CharField(max_length=25,blank=True)

class hdfc_mermpr_refund_excel_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Approve_Code=models.CharField(max_length=10,blank=True)
    Order_Id=models.CharField(max_length=50)
    Transaction_Id=models.CharField(max_length=50)
    Bank_Ref_Id=models.CharField(max_length=50)
    Payable_Merchant=models.FloatField(blank=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Arn_No=models.CharField(max_length=50,blank=True)
    Card_No=models.CharField(max_length=25,blank=True)
    MID=models.CharField(max_length=10,blank=True)
    Tid=models.CharField(max_length=15,blank=True)
    Remarks=models.CharField(max_length=250,blank=True)
    Refund_Type=models.CharField(max_length=15,blank=True)
    Sequence_Number=models.CharField(max_length=25,blank=True)

class hdfc_mermpr_mpp_sale_excel_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Approve_Code=models.CharField(max_length=50,blank=True)
    Order_Id=models.CharField(max_length=50)
    Transaction_Id=models.CharField(max_length=50)
    Payable_Merchant=models.FloatField(blank=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Arn_No=models.CharField(max_length=150,blank=True)
    Card_No=models.CharField(max_length=125,blank=True)
    MID=models.CharField(max_length=10,blank=True)
    Tid=models.CharField(max_length=50,blank=True)
    Remarks=models.CharField(max_length=250,blank=True,null=True)
    Sequence_Number=models.CharField(max_length=25,blank=True,null=True)

class hdfc_mermpr_mpp_refund_excel_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Approve_Code=models.CharField(max_length=50,blank=True)
    Order_Id=models.CharField(max_length=50)
    Transaction_Id=models.CharField(max_length=50)
    Bank_Ref_Id=models.CharField(max_length=50)
    Payable_Merchant=models.FloatField(blank=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Arn_No=models.CharField(max_length=150,blank=True)
    Card_No=models.CharField(max_length=125,blank=True)
    MID=models.CharField(max_length=10,blank=True)
    Tid=models.CharField(max_length=50,blank=True)
    Remarks=models.CharField(max_length=250,blank=True,null=True)
    Refund_Type=models.CharField(max_length=15,blank=True,null=True)
    Sequence_Number=models.CharField(max_length=25,blank=True,null=True)
    
   
class icici_mermpr_temp(models.Model):
    
    MID=models.CharField(max_length=15,blank=True)
    Card_Category=models.CharField(max_length=30,blank=True,null=True)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Dat=models.CharField(max_length=25,blank=True,null=True)
    Payable_Merchant=models.FloatField(blank=True)
    Credit_Debit=models.CharField(max_length=50,blank=True,null=True)
    Arn_No=models.CharField(max_length=50,blank=True,null=True)
    Card_No=models.CharField(max_length=25,blank=True,null=True)
    Approve_Code=models.CharField(max_length=25,blank=True,null=True)
    Transaction_Id=models.CharField(max_length=50,)
    Order_Id=models.CharField(max_length=50)
    Transaction_status=models.CharField(max_length=25,blank=True,null=True)
    Transaction_typ=models.CharField(max_length=25,blank=True,null=True) 
    Suc=models.FloatField(blank=True,null=True)
       
    def __str__(self):
        return self.Order_Id      

#------------------------ICICI PG AND MPP 03 MAY 2023--------------------------------

class icici_mermpr_pg_mpp_temp(models.Model):
    
    Super_mid=models.CharField(max_length=15,blank=True)
    MID=models.CharField(max_length=15,blank=True)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Card_no=models.CharField(max_length=25,blank=True,null=True)
    card_Category=models.CharField(max_length=30,blank=True,null=True)
    Auth_Code=models.CharField(max_length=25,blank=True,null=True)
    Transaction_type=models.CharField(max_length=25,blank=True,null=True)
    Net_Amount=models.FloatField(blank=True)
    Credit_Debit=models.CharField(max_length=50,blank=True,null=True)
    Transaction_Id=models.CharField(max_length=50,blank=True,null=True)
    Order_Id=models.CharField(max_length=50,blank=True,null=True)
    Arn_No=models.CharField(max_length=50,blank=True,null=True)
    Transaction_status=models.CharField(max_length=25,blank=True,null=True)
    Ret_Ref_No=models.CharField(max_length=50,blank=True,null=True)

class Indus_net_stement_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Dat=models.CharField(max_length=25,blank=True,null=True)
    Bank_Ref_No=models.CharField(max_length=25,blank=True,null=True)
    Narration=models.CharField(max_length=100,blank=True,null=True)
    Type=models.CharField(max_length=10,blank=True,null=True)
    Debit=models.FloatField(blank=True,null=True)
    Credit=models.FloatField(blank=True,null=True)
    Balance_Amount=models.CharField(max_length=20,blank=True,null=True)

class yesbank_mpr_stement_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Dat=models.CharField(max_length=25,blank=True,null=True)
    Description=models.CharField(max_length=100,blank=True,null=True)
    Reference_Id=models.CharField(max_length=50,blank=True,null=True)
    Debit=models.CharField(max_length=25,blank=True,null=True)
    Credit=models.CharField(max_length=25,blank=True,null=True)
    Balance_Amount=models.CharField(max_length=100,blank=True,null=True)

class yesbank_mpr_stement_temp_new(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Value_Date=models.CharField(max_length=25,blank=True,null=True)
    Description=models.CharField(max_length=300,blank=True,null=True)
    Txn_Literal=models.CharField(max_length=50,blank=True,null=True)
    Cheque_number=models.CharField(max_length=50,blank=True,null=True)
    Reference_Id=models.CharField(max_length=50,blank=True,null=True)
    Ref_user_no=models.CharField(max_length=25,blank=True,null=True)
    Debit_credit_type=models.CharField(max_length=10,blank=True,null=True)
    Orign_brn=models.CharField(max_length=25,blank=True,null=True)
    Amount=models.CharField(max_length=25,blank=True,null=True)
    Balance_Amount=models.CharField(max_length=25,blank=True,null=True)

class sbi_airnet_stement_temp(models.Model):
    
    Transaction_Date=models.DateField(blank=True,null=True)
    Value_Date=models.DateField(blank=True,null=True)
    Narration=models.CharField(max_length=250,blank=True,null=True)
    Cheque_No=models.CharField(max_length=250,blank=True,null=True)
    Branch_code=models.CharField(max_length=10,blank=True,null=True)
    Debit=models.FloatField(blank=True,null=True)
    Credit=models.FloatField(blank=True,null=True)
    Balance_Amount=models.FloatField(blank=True,null=True)

class union_net_stement_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Narration=models.CharField(max_length=100,blank=True,null=True)
    Cheque_No=models.CharField(max_length=10,blank=True,null=True)
    Debit=models.FloatField(blank=True,null=True)
    Credit=models.FloatField(blank=True,null=True)
    Balance_Amount=models.CharField(max_length=20,blank=True,null=True)

class karnataka_net_stement_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Narration=models.CharField(max_length=250,blank=True,null=True)
    Debit=models.FloatField(blank=True,null=True)
    Credit=models.FloatField(blank=True,null=True)
    Balance_Amount=models.CharField(max_length=15,blank=True,null=True)

class Amex_Mer_Mpr_temp(models.Model):
       
    Current_Date=models.CharField(max_length=50,blank=True,null=True)
    Settle_Date=models.CharField(max_length=25,blank=True,null=True)
    Tran_Id=models.CharField(max_length=125,blank=True,null=True)
    Record_Type=models.CharField(max_length=15,blank=True,null=True)
    Account_Number=models.CharField(max_length=25,blank=True,null=True)
    Submission_Name=models.CharField(max_length=50,blank=True,null=True)
    Terminal_Number=models.CharField(max_length=25,blank=True,null=True)
    Batch_Number=models.CharField(max_length=25,blank=True,null=True)
    Submission_Branch=models.CharField(max_length=25,blank=True,null=True)
    Trans_Date=models.CharField(max_length=25,blank=True,null=True)
    Card_Number=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Account_Number=models.CharField(max_length=25,blank=True,null=True)
    Payee_Name=models.CharField(max_length=75,blank=True,null=True)
    Submission_Date=models.CharField(max_length=25,blank=True,null=True)
    Processing_Date=models.CharField(max_length=25,blank=True,null=True)
    Airline_Ticket_Number=models.CharField(max_length=25,blank=True,null=True)
    Passeenger_Name=models.CharField(max_length=25,blank=True,null=True)
    Roc_Calculated_Count=models.TextField(max_length=25,blank=True,null=True)	
    Charge_Amount=models.FloatField(blank=True,null=True)		
    Submission_Amount=models.TextField(max_length=25,blank=True,null=True)			
    Payment_Debit_Amount=models.TextField(max_length=25,blank=True,null=True)			
    Settlement_Credit_Amount=models.TextField(max_length=25,blank=True,null=True)		 
    Settlement_Discount_Amount=models.TextField(max_length=25,blank=True,null=True)			
    Settlement_Service_Fee=models.TextField(max_length=25,blank=True,null=True)			
    Eexport_Report_igst=models.TextField(max_length=25,blank=True,null=True)	
    Export_Report_cgst=models.TextField(max_length=25,blank=True,null=True)		
    Export_Report_sgst=models.TextField(max_length=25,blank=True,null=True)		
    Settlement_Net_Amount=models.TextField(max_length=25,blank=True,null=True)		
    Submission_Total_Amount=models.TextField(max_length=25,blank=True,null=True)	
    Currency_Code=models.CharField(max_length=10,blank=True,null=True)
    Trans_Type=models.CharField(max_length=25,blank=True,null=True)
    Rejection_reason=models.CharField(max_length=25,blank=True,null=True)

class Indus_mer_mpr_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Tran_Id=models.CharField(max_length=125,blank=True,null=True)
    Gross_Amount=models.FloatField(blank=True,null=True)
    Order_id=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Account_Number=models.CharField(max_length=25,blank=True,null=True)
    Remarks=models.CharField(max_length=100,blank=True,null=True)
    Bank_Refund_No=models.CharField(max_length=25,blank=True,null=True)
    Payu_id=models.CharField(max_length=25,blank=True,null=True)
    Utr_No=models.CharField(max_length=55,blank=True,null=True)
    Trans_Type=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Amount=models.TextField(max_length=25,blank=True,null=True)


class sbi_mpr_mer_statement_temp(models.Model):

    Transaction_Date=models.DateField(blank=True,null=True)
    Value_Date=models.DateField(blank=True,null=True)
    Narration=models.CharField(max_length=250,blank=True,null=True)
    Cheque_No=models.CharField(max_length=250,blank=True,null=True)
    Branch_code=models.CharField(max_length=10,blank=True,null=True)
    Debit=models.FloatField(blank=True,null=True)
    Credit=models.FloatField(blank=True,null=True)
    Balance_Amount=models.FloatField(blank=True,null=True)

class sbi_mpr_mer_mprsale_temp(models.Model):
    Transaction_Date=models.DateField(blank=True,null=True)
    Tran_Id=models.CharField(max_length=25,blank=True,null=True)
    Order_id=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Amount=models.FloatField(blank=True,null=True)
    Settlement_Date=models.DateField(blank=True,null=True)
    Account_Number=models.CharField(max_length=25,blank=True,null=True)
    user_1=models.CharField(max_length=10,blank=True,null=True)




class fed_mpr_mer_statement_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Value_Date=models.CharField(max_length=25,blank=True,null=True)
    Narration=models.CharField(max_length=250,blank=True,null=True)
    Tran_Type=models.CharField(max_length=25,blank=True,null=True)
    Tran_id=models.CharField(max_length=25,blank=True,null=True)
    Cheque_No=models.CharField(max_length=25,blank=True,null=True)
    Debit=models.FloatField(blank=True,null=True)
    Credit=models.FloatField(blank=True,null=True)
    Balance_Amount=models.FloatField(blank=True,null=True)
    Dr_Cr_type=models.CharField(max_length=25,blank=True,null=True)

class karur_vysya_mpr_sale_temp(models.Model):

    serial_no=models.CharField(max_length=25,blank=True,null=True)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Booking_amount=models.FloatField(blank=True,null=True)
    Credited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)

class karur_vysya_mpr_refund_temp(models.Model):

    serial_no=models.CharField(max_length=25,blank=True,null=True)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_refund_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.FloatField(blank=True,null=True)
    Debited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)

# ---------------mer 08 jun 2022----------------------
class Indus_mer_mpr_test(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_id=models.CharField(max_length=25,blank=True,null=True)
    Tran_Id=models.CharField(max_length=125,blank=True,null=True)
    Booking_Amount=models.FloatField(max_length=25,blank=True,null=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Account_Number=models.CharField(max_length=25,blank=True,null=True)
    Remarks=models.CharField(max_length=100,blank=True,null=True)
    Bank_Refund_No=models.CharField(max_length=125,blank=True,null=True)
    Payu_id=models.CharField(max_length=25,blank=True,null=True)
    Utr_No=models.CharField(max_length=55,blank=True,null=True)
    Trans_Type=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Amount=models.FloatField(max_length=25,blank=True,null=True)

#----------14 Jul 2022 -------------------

class Amex_Mer_Mpr_web_temp(models.Model):
       
    Current_Date=models.CharField(max_length=50,blank=True,null=True)
    Settle_Date=models.CharField(max_length=25,blank=True,null=True)
    Tran_Id=models.CharField(max_length=125,blank=True,null=True)
    Record_Type=models.CharField(max_length=15,blank=True,null=True)
    Terminal_Number=models.CharField(max_length=25,blank=True,null=True)
    Trans_Date=models.CharField(max_length=25,blank=True,null=True)
    Card_Number=models.CharField(max_length=25,blank=True,null=True)
    Charge_Amount=models.CharField(max_length=25,blank=True,null=True)		
    Currency_Code=models.CharField(max_length=10,blank=True,null=True)
    Bank_ref_Id=models.CharField(max_length=25,blank=True,null=True)
    Order_Id=models.CharField(max_length=25,blank=True,null=True)

#--------------------15 JUL 2022--------------------- 

class icici_net_mpr_sale_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    prn_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Booking_amount=models.FloatField(blank=True,null=True)
    Credited_date=models.CharField(max_length=25,blank=True,null=True)
    
class icici_net_mpr_refund_temp(models.Model):

    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Cancellation_Type=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.CharField(max_length=25,blank=True,null=True)
    Bank_refund_ref_no=models.CharField(max_length=25,blank=True,null=True)
    status=models.CharField(max_length=25,blank=True,null=True)
    Debited_date=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Txn_Amount=models.CharField(max_length=25,blank=True,null=True)
    Cancelaltion_Id=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)


# ------------18-JUL-2022 ---------------------------------  

class south_indian_mpr_sale_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Booking_amount=models.FloatField(blank=True,null=True)
    Credited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)

class south_indian_mpr_refund_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_refund_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.FloatField(blank=True,null=True)
    Debited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)

#-----------------------19-JUL-2022 - SBI NEPAL-------------------

class sbi_nepal_mpr_sale_temp(models.Model):

    Transaction_Date=models.DateField(blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Booking_amount=models.FloatField(blank=True,null=True)
    Credited_date=models.DateField(blank=True,null=True)
   
class sbi_nepal_mpr_refund_temp(models.Model):

    Transaction_Date=models.DateField(blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_refund_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.FloatField(blank=True,null=True)
    Debited_date=models.DateField(blank=True,null=True)


#-------------------30-SEP-2022---------------------------------------------

class Central_bank_mpr_sale_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Booking_amount=models.FloatField(blank=True,null=True)
    Credited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)
    Bank_Charge=models.CharField(max_length=25,blank=True,null=True)
    Service_Charge=models.CharField(max_length=25,blank=True,null=True)
    Total_amount=models.FloatField(blank=True,null=True)
    UDF1=models.CharField(max_length=25,blank=True,null=True)

class Central_bank_mpr_refund_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_refund_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.FloatField(blank=True,null=True)
    Debited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)

#----------01 Aug 2022 -------------------

class Amex_Mer_Mpr_mpp_sale_temp(models.Model):
       
    Current_Date=models.CharField(max_length=50,blank=True,null=True)
    Settle_Date=models.CharField(max_length=25,blank=True,null=True)
    Tran_Id=models.CharField(max_length=125,blank=True,null=True)
    Record_Type=models.CharField(max_length=15,blank=True,null=True)
    Terminal_Number=models.CharField(max_length=25,blank=True,null=True)
    Trans_Date=models.CharField(max_length=25,blank=True,null=True)
    Card_Number=models.CharField(max_length=25,blank=True,null=True)
    Charge_Amount=models.CharField(max_length=25,blank=True,null=True)		
    Currency_Code=models.CharField(max_length=10,blank=True,null=True)
    Order_Id=models.CharField(max_length=25,blank=True,null=True)


class Amex_Mer_Mpr_mpp_refund_temp(models.Model):
       
    Current_Date=models.CharField(max_length=50,blank=True,null=True)
    Settle_Date=models.CharField(max_length=25,blank=True,null=True)
    Bank_ref_Id=models.CharField(max_length=25,blank=True,null=True)
    Tran_Id=models.CharField(max_length=125,blank=True,null=True)
    Record_Type=models.CharField(max_length=15,blank=True,null=True)
    Terminal_Number=models.CharField(max_length=25,blank=True,null=True)
    Trans_Date=models.CharField(max_length=25,blank=True,null=True)
    Card_Number=models.CharField(max_length=25,blank=True,null=True)
    Charge_Amount=models.CharField(max_length=25,blank=True,null=True)		
    Currency_Code=models.CharField(max_length=10,blank=True,null=True)
    Order_Id=models.CharField(max_length=25,blank=True,null=True)

#-------------------11-OCT-2022---KOTAK RUPAY CARD NEW ------------------------------------------

class Kotak_mer_rupay_mpr_sale_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Merchant_id=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Booking_amount=models.FloatField(blank=True,null=True)
    Credited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    Card_program=models.CharField(max_length=25,blank=True,null=True)
    Card_scheme=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)
    

class Kotak_mer_rupay_mpr_refund_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Merchant_id=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_refund_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Irctc_can_id=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.FloatField(blank=True,null=True)
    Debited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    Card_program=models.CharField(max_length=25,blank=True,null=True)
    Card_scheme=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)

#-------------------10-MAY-2023---KOTAK NET BANK ------------------------------------------

class Kotak_mer_nbweb_mpr_sale_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Booking_amount=models.FloatField(blank=True,null=True)
    Credited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)
    

class Kotak_mer_nbweb_mpr_refund_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_refund_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Irctc_can_id=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.FloatField(blank=True,null=True)
    Debited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)

# -----------------------03-NOV-2022---------------------------------

class federal_mpr_sale_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=100,blank=True,null=True)
    Booking_amount=models.CharField(max_length=25,blank=True,null=True)
    Credited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=50,blank=True,null=True)

class federal_mpr_refund_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_refund_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.CharField(max_length=25,blank=True,null=True)
    Debited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)

#-------------------HDFC PG WEB -------------18 NOV 2022 ---------------------------------------

class hdfc_mermpr_web_sale_temp(models.Model):
    
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Approve_Code=models.CharField(max_length=10,blank=True)
    Order_Id=models.CharField(max_length=50)
    Transaction_Id=models.CharField(max_length=50)
    Payable_Merchant=models.FloatField(blank=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Arn_No=models.CharField(max_length=50,blank=True)
    Card_No=models.CharField(max_length=25,blank=True)
    MID=models.CharField(max_length=10,blank=True)
    Tid=models.CharField(max_length=15,blank=True)
    Remarks=models.CharField(max_length=25,blank=True)
    Sale_pg_id=models.CharField(max_length=25,blank=True)
    
   
class hdfc_mermpr_web_refund_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Approve_Code=models.CharField(max_length=10,blank=True)
    Order_Id=models.CharField(max_length=50)
    Transaction_Id=models.CharField(max_length=50)
    Bank_Ref_Id=models.CharField(max_length=50)
    Payable_Merchant=models.FloatField(blank=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Arn_No=models.CharField(max_length=50,blank=True)
    Card_No=models.CharField(max_length=25,blank=True)
    MID=models.CharField(max_length=10,blank=True)
    Tid=models.CharField(max_length=15,blank=True)
    Remarks=models.CharField(max_length=25,blank=True)
    Refund_Type=models.CharField(max_length=15,blank=True)
    Refund_pg_id=models.CharField(max_length=25,blank=True)


#-------------------------24-aug-2022------------AIR ICICI--------------------

class Air_icici_Mer_Mpr_temp(models.Model):

    Transaction_type=models.CharField(max_length=10,blank=True,null=True)
    Order_Id=models.CharField(max_length=50,null=True)
    Fraud_Status=models.CharField(max_length=50,null=True)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Gross_Amount=models.CharField(max_length=25,blank=True,null=True)
    TDR_percentage=models.CharField(max_length=25,blank=True,null=True)
    TDR_Amount=models.CharField(max_length=25,blank=True,null=True)
    Tax_Amount=models.CharField(max_length=25,blank=True,null=True)
    Payable_Amount=models.CharField(max_length=25,blank=True,null=True)
    CCAvenue_Ref_Number=models.CharField(max_length=100,blank=True,null=True)
    Auth_Code=models.CharField(max_length=100,blank=True,null=True)
    td_type=models.CharField(max_length=15,blank=True,null=True)
    Payout_ID=models.CharField(max_length=15,blank=True,null=True)	
    Payments_Type=models.CharField(max_length=25,blank=True,null=True)	
    Card_Name=models.CharField(max_length=50,blank=True,null=True)	
    Invoice_No=models.CharField(max_length=15,blank=True,null=True)
    order_bin_country=models.CharField(max_length=15,blank=True,null=True)	
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    MID=models.CharField(max_length=50,blank=True,null=True)
    Shipped_Date=models.CharField(max_length=25,blank=True,null=True) 

#-------------26-aug-2022 -------------INDIAN BANK --------------------

class indian_mpr_sale_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=100,blank=True,null=True)
    Booking_amount=models.CharField(max_length=25,blank=True,null=True)
    Credited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=50,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)

class indian_mpr_refund_temp(models.Model):

    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Cancellation_id=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.CharField(max_length=25,blank=True,null=True)
    Debited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=25,blank=True,null=True)

#---------------------------PNB -----15-FEB-2023-----------------------------------------

class pnb_mpr_sale_temp(models.Model):

    Serial_no=models.CharField(max_length=25,blank=True,null=True)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=100,blank=True,null=True)
    Booking_amount=models.CharField(max_length=25,blank=True,null=True)
    Credited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=50,blank=True,null=True)
    remarks=models.CharField(max_length=100,blank=True,null=True)

class pnb_mpr_refund_temp(models.Model):

    Serial_no=models.CharField(max_length=25,blank=True,null=True)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Order_no=models.CharField(max_length=25,blank=True,null=True)
    Bank_booking_ref_no=models.CharField(max_length=25,blank=True,null=True)
    Cancellation_id=models.CharField(max_length=25,blank=True,null=True)
    Refund_amount=models.CharField(max_length=25,blank=True,null=True)
    Debited_date=models.CharField(max_length=25,blank=True,null=True)
    Cus_account_no=models.CharField(max_length=25,blank=True,null=True)
    remarks=models.CharField(max_length=100,blank=True,null=True)


# ---------------------DISPUTE TRACKING SYSTEM TABLE -------------------------

class Tracking_Reg(models.Model):

    Reg_Date = models.DateField()
    Complaint= models.CharField(max_length=50,blank=True,null=True)
    Bank= models.CharField(max_length=50,blank=True,null=True)
    Remarks= models.TextField(blank=True,null=True)
    Follow_Date= models.TextField(blank=True,null=True)
    Closing_Date = models.CharField(max_length=50,blank=True,null=True)
    Closing_Remarks= models.TextField(blank=True,null=True)
    Dispute_Amount=models.FloatField(blank=True,null=True)
    Email_subject=models.CharField(max_length=150,blank=True,null=True)
    Bank_Response=models.TextField(blank=True,null=True)
    Bank_Res_Date=models.CharField(max_length=50,blank=True,null=True)
    Amont_Recovered=models.FloatField(blank=True,null=True)
    Txn_Date=models.DateField(blank=True,null=True)
    Txn_id=models.TextField(blank=True,null=True)
    Status=models.CharField(max_length=50,blank=True,null=True)
    user_name=models.CharField(max_length=50,blank=True,null=True)
    Merchant_name=models.CharField(max_length=50,blank=True,null=True)



#-------------------------Bank Statement Merchant --------------------06-sep-2022---------------

class Bank_Statement_Merchant(models.Model):

    Trans_Date=models.DateField(blank=True,null=True)
    Value_Date=models.DateField(blank=True,null=True)
    Description=models.CharField(max_length=200,blank=True,null=True)
    Cheque_Number=models.CharField(max_length=200,blank=True,null=True)
    Branch_code=models.CharField(max_length=20,blank=True,null=True)
    Branch_Name=models.CharField(max_length=100,blank=True,null=True)
    Credit_Debit_type=models.CharField(max_length=20,blank=True,null=True)
    Amount=models.FloatField(blank=True,null=True)
    Credit_Amount=models.FloatField(blank=True,null=True)
    Debit_Amount=models.FloatField(blank=True,null=True)
    Balance_Amount=models.FloatField(blank=True,null=True)
    Account_number=models.CharField(max_length=20)
    Remarks=models.CharField(max_length=150)
    File_number=models.CharField(max_length=150,blank=True,null=True)
    File_upload_date=models.DateField()
    Recon_status=models.CharField(max_length=20,blank=True,null=True)
    Recon_remarks=models.CharField(max_length=20,blank=True,null=True)
    Bank_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Bank_Match_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Record_Number=models.CharField(max_length=20,blank=True,null=True)
    Journl_Number=models.CharField(max_length=20,blank=True,null=True)
    Txn_code=models.CharField(max_length=20,blank=True,null=True)
    Drcr_Account_number=models.CharField(max_length=20,blank=True,null=True)
    Teller=models.CharField(max_length=20,blank=True,null=True)
    Narration=models.CharField(max_length=200,blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True)  
    Ledger_balance=models.FloatField(blank=True,null=True)

   
#-------------------------Bank Statement Nodal ---------------------06-sep-2022------------------

class Bank_Statement_Nodal(models.Model):

    Trans_Date=models.DateField(blank=True,null=True)
    Value_Date=models.DateField(blank=True,null=True)
    Description=models.CharField(max_length=200,blank=True,null=True)
    Cheque_Number=models.CharField(max_length=200,blank=True,null=True)
    Branch_code=models.CharField(max_length=20,blank=True,null=True)
    Branch_Name=models.CharField(max_length=100,blank=True,null=True)
    Credit_Debit_type=models.CharField(max_length=20,blank=True,null=True)
    Amount=models.FloatField(blank=True,null=True)
    Credit_Amount=models.FloatField(blank=True,null=True)
    Debit_Amount=models.FloatField(blank=True,null=True)
    Balance_Amount=models.FloatField(blank=True,null=True)
    Account_number=models.CharField(max_length=20)
    Remarks=models.CharField(max_length=150)
    File_number=models.CharField(max_length=150,blank=True,null=True)
    File_upload_date=models.DateField()
    Recon_status=models.CharField(max_length=20,blank=True,null=True)
    Recon_remarks=models.CharField(max_length=20,blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True)  
    Bank_Summary_Trans=models.CharField(max_length=10,blank=True,null=True)


# --------------------------------LEDGER TABLE ------11-SEP-2023 ---------------------------------


class ledger_mer_credit(models.Model): 

    Transaction_Date=models.DateField(blank=True)
    Receivable_Sale_Amount=models.FloatField(blank=True,null=True)
    Payable_Refund_Amount=models.FloatField(blank=True,null=True)
    Net_Amount=models.FloatField(blank=True,null=True)
    Trans_Type=models.CharField(max_length=25,blank=True)
    Settlement_Type=models.CharField(max_length=25,blank=True)
    Bank_Id=models.CharField(max_length=25,blank=True,null=True)
    Bank_Name=models.CharField(max_length=50,blank=True,null=True)
    Account_number=models.CharField(max_length=50,blank=True,null=True)
    Bank_Date=models.DateField(blank=True,null=True)
    Bank_credit_Amount=models.FloatField(blank=True,null=True)
    Bank_debit_Amount=models.FloatField(blank=True,null=True)
    Bank_Description=models.CharField(max_length=150,blank=True,null=True)
    Bank_Remarks=models.CharField(max_length=150,blank=True,null=True)
    Other_credit_Amount=models.FloatField(blank=True,null=True)
    Other_debit_Amount=models.FloatField(blank=True,null=True)
    Other_Description=models.CharField(max_length=100,blank=True,null=True)
    Other_Remarks=models.CharField(max_length=100,blank=True,null=True)
    update_Date=models.DateTimeField(blank=True,null=True)
    update_user=models.CharField(max_length=25,blank=True,null=True)
    Description=models.CharField(max_length=100,blank=True,null=True)
    Remarks=models.CharField(max_length=100,blank=True,null=True)
    Mpr_Settlement_Date=models.DateField(blank=True,null=True)
    mpr_credit_debit_Date=models.DateField(blank=True,null=True)
    Mpr_sale_Amount=models.FloatField(blank=True,null=True)
    Mpr_Refund_Amount=models.FloatField(blank=True,null=True)
    Mpr_net_Amount=models.FloatField(blank=True,null=True)
    Mpr_Remarks=models.CharField(max_length=100,blank=True,null=True)
    Db_Actual_Credit_Debit_Date=models.DateField(blank=True,null=True)
    Trans_From=models.CharField(max_length=25,blank=True,null=True)


#-------------------TOURISM -------------------04 APR 2024-------------------------
    
class Tour_Ticket_Sale(models.Model):

    Reservation_Id=models.CharField(max_length=50)
    Booking_Date=models.DateField()
    Bank_Txn_Number=models.CharField(max_length=50)
    Billdesk_id=models.CharField(max_length=50,blank=True,null=True)
    Sale_Amount=models.FloatField(blank=True)
    Bank_id=models.CharField(max_length=10)
    Bank_Name=models.CharField(max_length=25,blank=True)
    product_mode=models.CharField(max_length=125,blank=True,null=True) 
    product_name=models.CharField(max_length=25,blank=True,null=True) 
    Bank_Name_ref=models.CharField(max_length=125,blank=True)
    product_type=models.CharField(max_length=25,blank=True,null=True) 
    bank_extra_ref=models.CharField(max_length=50,blank=True,null=True)
    Entity_Code=models.CharField(max_length=10,blank=True,null=True)
    Actual_Credit_Date=models.DateField(blank=True,null=True)
    Sale_Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Credit_Amount=models.FloatField(blank=True,null=True)
    File_upload_Date=models.DateTimeField(blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True) 
    Db_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Match_Summary_Trans=models.CharField(max_length=10,blank=True,null=True)  
    mpr_trans_status=models.CharField(max_length=25,blank=True,null=True)
    
    
    def __str__(self):
        return self.Reservation_Id

class Tour_Ticket_Refund(models.Model):

    Reservation_Id=models.CharField(max_length=50)
    Transaction_Date=models.DateField()
    Bank_Txn_Id=models.CharField(max_length=50,blank=True,null=True)
    Refund_Amount=models.FloatField(blank=True)
    Refund_Status=models.CharField(max_length=10,blank=True,null=True)
    Bank_id=models.CharField(max_length=5,blank=True,null=True)
    Bank_Name=models.CharField(max_length=25,blank=True,null=True)
    Actual_Refund_Date=models.DateField(blank=True,null=True)
    product_name=models.CharField(max_length=25,blank=True,null=True) 
    Refundt_type=models.CharField(max_length=25,blank=True,null=True)
    Transaction_type=models.CharField(max_length=25,blank=True,null=True)
    product_type=models.CharField(max_length=25,blank=True,null=True) 
    bank_extra_ref=models.CharField(max_length=50,blank=True,null=True)
    Actual_Debit_Date=models.DateField(blank=True,null=True)
    Refund_Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Reversal_Date1=models.DateField(blank=True,null=True)
    Reversal_Date2=models.DateField(blank=True,null=True)
    Reversal_Status=models.CharField(max_length=10,blank=True,null=True)
    Debit_Amount=models.FloatField(blank=True,null=True)
    Reversal_Amount=models.FloatField(blank=True,null=True)
    Reversal1_Amount=models.FloatField(blank=True,null=True)
    File_upload_Date=models.DateTimeField(blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True) 
    Db_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Match_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    mpr_trans_status=models.CharField(max_length=25,blank=True,null=True)
    
     

    def __str__(self):
        return self.Reservation_Id
    
class irctc_tourism_Mpr(models.Model):

    Merchant_Name=models.CharField(max_length=50,blank=True,null=True)
    MID=models.CharField(max_length=50,blank=True)
    Transaction_Id=models.CharField(max_length=50,blank=True,null=True)
    Order_Id=models.CharField(max_length=50,blank=True,null=True)
    Transaction_Date=models.DateField(blank=True,null=True)
    Settlement_Date=models.DateField()
    Refund_Request_Date=models.DateField(blank=True,null=True)
    Transaction_type=models.CharField(max_length=50,blank=True)
    Domestic_Amount=models.FloatField(blank=True,null=True)
    Intl_Amount=models.FloatField(blank=True,null=True)
    Acquirer_Comm=models.FloatField(blank=True,null=True)
    Payable_Merchant=models.FloatField(blank=True)
    UDF1=models.CharField(max_length=150,blank=True,null=True)
    BankName_Receive_Funds=models.CharField(max_length=50,blank=True,null=True)
    Merchant_code=models.CharField(max_length=50,blank=True,null=True)
    Rec_Fmt=models.CharField(max_length=50,blank=True,null=True)
    Acquirer_Name=models.CharField(max_length=50,blank=True,null=True)
    Refund_Flag=models.CharField(max_length=10,blank=True,null=True)
    Payments_Type=models.CharField(max_length=50,blank=True,null=True)
    MOP_Type=models.CharField(max_length=50,blank=True,null=True)
    Credit_Debit_Date=models.DateField(blank=True,null=True)
    Bank_Name=models.CharField(max_length=15,blank=True,null=True)
    Refund_Order_Id=models.CharField(max_length=50,blank=True,null=True)
    tourismsale=models.ForeignKey(
       Tour_Ticket_Sale,null=True, on_delete=models.CASCADE,
            related_name='tourismsale')
    tourismrefund=models.ForeignKey(
        Tour_Ticket_Refund,null=True, on_delete=models.CASCADE,
            related_name='tourismrefund')
    Acq_Id=models.CharField(max_length=125,blank=True,null=True)
    Approve_code=models.CharField(max_length=15,blank=True,null=True)
    Arn_No=models.CharField(max_length=125,blank=True,null=True)
    Card_No=models.CharField(max_length=50,blank=True,null=True)
    Tid=models.CharField(max_length=25,blank=True,null=True)
    Remarks=models.CharField(max_length=50,blank=True,null=True)
    Bank_Ref_id=models.CharField(max_length=125,blank=True,null=True)
    File_upload_Date=models.DateTimeField(blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True)
    Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Mpr_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Mpr_Match_Summary_Trans=models.CharField(max_length=10,blank=True,null=True) 
    Card_type=models.CharField(max_length=100,blank=True,null=True)
    GST_Number=models.CharField(max_length=50,blank=True,null=True)
    Gross_Amount=models.FloatField(blank=True,null=True)
    Aggregator_Com=models.FloatField(blank=True,null=True)
    Payout_from_Nodal=models.CharField(max_length=50,blank=True,null=True)
    Nodal_Account_No=models.CharField(max_length=50,blank=True,null=True)
    Aggregator_Name=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.Order_Id

    
class Tour_Ticket_Sale_test(models.Model):
    
    Reservation_Id=models.CharField(max_length=50)
    Booking_Date=models.DateField()
    Bank_Txn_Number=models.CharField(max_length=50)
    Billdesk_id=models.CharField(max_length=50,blank=True,null=True)
    Sale_Amount=models.FloatField(blank=True)
    Bank_id=models.CharField(max_length=10)
    Bank_Name=models.CharField(max_length=25,blank=True)
    product_mode=models.CharField(max_length=125,blank=True,null=True) 
    product_name=models.CharField(max_length=25,blank=True,null=True) 
    Bank_Name_ref=models.CharField(max_length=125,blank=True)
    product_type=models.CharField(max_length=25,blank=True,null=True) 
    bank_extra_ref=models.CharField(max_length=50,blank=True,null=True)
    Entity_Code=models.CharField(max_length=10,blank=True,null=True)
   
    
   
class Tour_Ticket_Refund_test(models.Model):

    Reservation_Id=models.CharField(max_length=50)
    Transaction_Date=models.DateField()
    Bank_Txn_Id=models.CharField(max_length=50,blank=True,null=True)
    Refund_Amount=models.FloatField(blank=True)
    Refund_Status=models.CharField(max_length=10,blank=True,null=True)
    Bank_id=models.CharField(max_length=5,blank=True,null=True)
    Bank_Name=models.CharField(max_length=25,blank=True,null=True)
    Actual_Refund_Date=models.DateField(blank=True,null=True)
    product_name=models.CharField(max_length=25,blank=True,null=True) 
    Refundt_type=models.CharField(max_length=25,blank=True,null=True)
    Transaction_type=models.CharField(max_length=25,blank=True,null=True)
    product_type=models.CharField(max_length=25,blank=True,null=True) 
    bank_extra_ref=models.CharField(max_length=50,blank=True,null=True)


class sbi_tournet_stement_temp(models.Model):
    
    Transaction_Date=models.DateField(blank=True,null=True)
    Value_Date=models.DateField(blank=True,null=True)
    Narration=models.CharField(max_length=250,blank=True,null=True)
    Cheque_No=models.CharField(max_length=250,blank=True,null=True)
    Branch_code=models.CharField(max_length=10,blank=True,null=True)
    Debit=models.FloatField(blank=True,null=True)
    Credit=models.FloatField(blank=True,null=True)
    Balance_Amount=models.FloatField(blank=True,null=True)

class Hdfc_tourism_Mpr_temp(models.Model):
    
    Merchant_Code=models.CharField(max_length=25,blank=True)
    Terminal_Number=models.CharField(max_length=25,blank=True)
    Rec_Fmt=models.CharField(max_length=25,blank=True)
    Bat_Nbr=models.CharField(max_length=15,blank=True)
    Card_Type=models.CharField(max_length=50,blank=True)
    Card_Number=models.CharField(max_length=25,blank=True)
    Trans_Date=models.DateField(blank=True,null=True)
    Settle_Date=models.DateField(blank=True,null=True)
    Approv_code=models.CharField(max_length=25,blank=True)
    Intnl_Amount=models.FloatField(blank=True,null=True)
    Domestic_Amount=models.FloatField(blank=True,null=True)
    Tran_Id=models.CharField(max_length=25,blank=True,null=True)
    Upvalue=models.CharField(max_length=25,blank=True,null=True)
    merchant_track_id=models.CharField(max_length=50,blank=True)
    Msf=models.CharField(max_length=25,blank=True,null=True)
    Serv_Tax=models.CharField(max_length=25,blank=True,null=True)
    Sb_Cess=models.CharField(max_length=25,blank=True,null=True)
    Kk_Cess=models.CharField(max_length=25,blank=True,null=True)
    CGST_Amount=models.CharField(max_length=25,blank=True,null=True)
    SGST_Amount=models.CharField(max_length=25,blank=True,null=True)
    IGST_Amount=models.CharField(max_length=25,blank=True,null=True)
    UTGST_Amount=models.CharField(max_length=25,blank=True,null=True)
    Net_Amount=models.FloatField(blank=True,null=True)
    Debit_Credit_Type=models.CharField(max_length=25,blank=True,null=True)
    UDF1=models.CharField(max_length=300,blank=True,null=True)
    UDF2=models.CharField(max_length=50,blank=True,null=True)
    UDF3=models.CharField(max_length=50,blank=True,null=True)
    UDF4=models.CharField(max_length=50,blank=True,null=True)
    UDF5=models.CharField(max_length=50,blank=True,null=True)
    Sequence_Number=models.CharField(max_length=25,blank=True,null=True)
    ARN_RRN_Number=models.CharField(max_length=50,blank=True,null=True)
    Invoice_Number=models.CharField(max_length=25,blank=True,null=True)
    GSTN_Transaction_Id=models.CharField(max_length=25,blank=True,null=True)
    Order_id=models.CharField(max_length=25,blank=True,null=True)





 # -------------------------------------------------------------OLD TABLE TO BE REMOVED ----------------------------------------
 # 
 
class Person(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=64,blank=False)
    email=models.EmailField()
    create=models.DateField()
    modify=models.DateField()
    reason=models.CharField(max_length=64,blank=True)
    def __str__(self):
        return self.username


class UPI_Details(models.Model):

    UPI_Merchant_Id=models.CharField(max_length=100,blank=True)
    Merchant_Name=models.CharField(max_length=150,blank=True)
    Merchant_Vpa=models.CharField(max_length=100,blank=True)
    Payer_Vpa=models.CharField(max_length=100,blank=True)
    ACQ_Id=models.CharField(max_length=25,blank=True)
    Pg_Ref_Num=models.CharField(max_length=100,blank=True)
    Txn_Ref_No_RRN=models.CharField(max_length=25,blank=True)
    Transaction_Req_Date=models.DateField(blank=True)
    Settlement_Date=models.DateField(blank=True)
    Currency=models.CharField(max_length=15,blank=True)
    Transaction_Amount=models.FloatField()
    MSF_Amount=models.FloatField(blank=True)
    CGST_Amount=models.FloatField(blank=True)
    SGST_Amount=models.FloatField(blank=True)
    IGST_Amount=models.FloatField(blank=True)
    UTGST_Amount=models.FloatField(blank=True)
    Net_Amount=models.FloatField(blank=True)
    Refund_Flag=models.CharField(max_length=25,blank=True)
    GST_Invoice_No=models.CharField(max_length=25,blank=True)
    Trans_Type=models.CharField(max_length=25,blank=True)
    Pay_Type=models.CharField(max_length=25,blank=True)
    CR_DR=models.CharField(max_length=25,blank=True)
    Bank_Name=models.CharField(max_length=15,blank=True)
    Nodal_Credit_Date=models.DateField(blank=True,null=True)
    transactiondetails=models.ForeignKey(
        Transaction_Details,null=True, on_delete=models.CASCADE,
        related_name='upidetails')

    def __str__(self):
        return self.Pg_Ref_Num



class Kotak_Mpr_tem(models.Model):

    Merchant_Code=models.CharField(max_length=25,blank=True)
    Terminal_Number=models.CharField(max_length=25,blank=True)
    Rec_Fmt=models.CharField(max_length=25,blank=True)
    Bat_Nbr=models.CharField(max_length=15,blank=True)
    Card_Type=models.CharField(max_length=25,blank=True)
    Card_Number=models.CharField(max_length=25,blank=True)
    Trans_Date=models.DateField(blank=True)
    Settle_Date=models.DateField(blank=True)
    Approv_code=models.CharField(max_length=25,blank=True)
    Intnl_Amount=models.FloatField(blank=True)
    Domestic_Amount=models.FloatField()
    Tran_Id=models.CharField(max_length=25,blank=True)
    Upvalue=models.CharField(max_length=25,blank=True)
    Pg_Ref_Num=models.CharField(max_length=25,blank=True)
    Msf=models.FloatField(blank=True)
    Serv_Tax=models.FloatField(blank=True)
    Sb_Cess=models.FloatField(blank=True)
    Kk_Cess=models.FloatField(blank=True)
    CGST_Amount=models.FloatField(blank=True)
    SGST_Amount=models.FloatField(blank=True)
    IGST_Amount=models.FloatField(blank=True)
    UTGST_Amount=models.FloatField(blank=True)
    Net_Amount=models.FloatField()
    Debit_Credit_Type=models.CharField(max_length=25,blank=True)
    UDF1=models.CharField(max_length=25,blank=True)
    UDF2=models.CharField(max_length=25,blank=True)
    UDF3=models.CharField(max_length=25,blank=True)
    UDF4=models.CharField(max_length=25,blank=True)
    UDF5=models.CharField(max_length=25,blank=True)
    Sequence_Number=models.CharField(max_length=25,blank=True)
    ARN_RRN_Number=models.CharField(max_length=50,blank=True)
    Invoice_Number=models.CharField(max_length=25,blank=True)
    GSTN_Transaction_Id=models.CharField(max_length=25,blank=True)

    def __str__(self):
        return self.Pg_Ref_Num

class Im_Close_Loop(models.Model):
    Hash_Id=models.CharField(max_length=100,blank=True,null=True)	
    Currency_Rate_Id=models.CharField(max_length=25,blank=True,null=True)	
    Points=models.FloatField(blank=True,null=True)		
    Amount=models.FloatField(blank=True,null=True)	
    Card_Fee=models.FloatField(blank=True,null=True)	
    Charge_Fee=models.FloatField(blank=True,null=True)	
    Grand_Total=models.FloatField(blank=True,null=True)
    PP=models.CharField(max_length=100,blank=True,null=True)	
    Payment_Ref=models.CharField(max_length=200,blank=True,null=True)	
    Status=models.CharField(max_length=25,blank=True,null=True)	
    Date_Updated=models.DateField(blank=True)	
    Date_Added=models.DateField(blank=True,null=True)	
    Details=models.CharField(max_length=500,blank=True,null=True)	
    Txn_Type=models.CharField(max_length=50,blank=True,null=True)		
    Dr_Cr=models.CharField(max_length=15,blank=True,null=True)		
    Is_Active=models.CharField(max_length=10,blank=True,null=True)		
    TT=models.CharField(max_length=10,blank=True,null=True)	
    Credit_Debit_Date=models.DateField(blank=True,null=True)
    Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Credit_debit_Amount=models.FloatField(blank=True,null=True)
    
    def __str__(self):
        return self.Payment_Ref
        
class Im_network(models.Model):
    Switch_Ref=models.CharField(max_length=100,blank=True,null=True)
    Vs_Ref=models.CharField(max_length=100,blank=True,null=True)
    Arn=models.CharField(max_length=100,blank=True,null=True)
    Txn_Date_Added=models.DateField(blank=True,null=True)
    Vs_Date=models.DateField(blank=True,null=True)
    Settlement_Date=models.DateField(blank=True,null=True)
    Bank_Txn_Date=models.DateField(blank=True,null=True)
    Txn_Amount=models.FloatField(blank=True,null=True)
    Settle_Amount=models.FloatField(blank=True,null=True)
    Op_Ref=models.CharField(max_length=100,blank=True,null=True)
    Op_Amount=models.FloatField(blank=True,null=True)
    Status=models.CharField(max_length=15,blank=True,null=True)
    Comments=models.CharField(max_length=15,blank=True,null=True)
    Card_Status=models.CharField(max_length=15,blank=True,null=True)
    Op_Date=models.DateField(blank=True,null=True)
    Txn_Type=models.CharField(max_length=15,blank=True,null=True)
    Credit_Debit_Date=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.Switch_Ref

class Im_Open_Loop(models.Model):
    Hash_Id=models.CharField(max_length=100,blank=True,null=True)
    Network=models.CharField(max_length=10,blank=True,null=True)
    Channel=models.CharField(max_length=10,blank=True,null=True)
    Card_Currency=models.CharField(max_length=5,blank=True,null=True)
    Total_Amount=models.FloatField(blank=True,null=True)
    Total_Currency=models.CharField(max_length=5,blank=True,null=True)
    Transaction_Type=models.CharField(max_length=25,blank=True,null=True)
    Merchant_Id=models.CharField(max_length=25,blank=True,null=True)
    Merchant_Name=models.CharField(max_length=100,blank=True,null=True)
    Response_Code=models.CharField(max_length=5,blank=True,null=True)
    Description=models.CharField(max_length=30,blank=True,null=True)
    Reversal_Description=models.CharField(max_length=100,blank=True,null=True)
    Revtxn_Date=models.DateField(blank=True,null=True)
    Released_Date=models.DateField(blank=True,null=True)
    Settlment_Date=models.DateField(blank=True,null=True)
    Date_Reversal=models.DateField(blank=True,null=True)
    Date_Added=models.DateField(blank=True,null=True)
    Rr_Number=models.CharField(max_length=15,blank=True,null=True)
    Txn_Type=models.CharField(max_length=10,blank=True,null=True)
    Dr_Cr=models.CharField(max_length=10,blank=True,null=True)
    Actual_Credit_Debit_Date=models.DateField(blank=True,null=True)
    Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Credit_debit_Amount=models.FloatField(blank=True,null=True)
  
    def __str__(self):
        return self.Hash_Id


class Ipay_Rail_Mpr_temp(models.Model):

    Merchant_Name=models.CharField(max_length=50,blank=True)
    MID=models.CharField(max_length=50,blank=True)
    Transaction_Id=models.CharField(max_length=50)
    Order_Id=models.CharField(max_length=50)
    Transaction_Date=models.CharField(max_length=25,blank=True,null=True)
    Settlement_Date=models.CharField(max_length=25,blank=True,null=True)
    Refund_Request_Date=models.CharField(max_length=25,blank=True,null=True)
    Transaction_type=models.CharField(max_length=10,blank=True)
    Gross_Amount=models.FloatField(blank=True)
    Aggregator_Com=models.FloatField(blank=True)
    Acquirer_Comm=models.FloatField(blank=True)
    Payable_Merchant=models.FloatField(blank=True)
    Payout_from_Nodal=models.FloatField(blank=True)
    BankName_Receive_Funds=models.CharField(max_length=50,blank=True)
    Nodal_Account_No=models.CharField(max_length=50,blank=True)
    Aggregator_Name=models.CharField(max_length=50,blank=True)
    Acquirer_Name=models.CharField(max_length=50,blank=True)
    Refund_Flag=models.CharField(max_length=10,blank=True)
    Payments_Type=models.CharField(max_length=10,blank=True)
    MOP_Type=models.CharField(max_length=50,blank=True)
    Refund_Order_Id=models.CharField(max_length=50,blank=True,null=True)
    Acq_Id=models.CharField(max_length=125,blank=True,null=True)
    
    def __str__(self):
        return self.Order_Id


class File_Name_Store_temp(models.Model):
    Date_Upload=models.DateField()	
    File_Name=models.CharField(max_length=300,blank=True,null=True)	
    User_name=models.CharField(max_length=25,blank=True,null=True)

    def __str__(self):
        return self.File_Name

# ---------------------------- 20-09-2021 ----------------------------------------

class Rail_nonunique_Mpr(models.Model):

    Merchant_Name=models.CharField(max_length=50,blank=True,null=True)
    MID=models.CharField(max_length=50,blank=True,null=True)
    Transaction_Id=models.CharField(max_length=50,null=True)
    Order_Id=models.CharField(max_length=50,null=True)
    Transaction_Date=models.DateField(blank=True,null=True)
    Settlement_Date=models.DateField(blank=True,null=True)
    Refund_Request_Date=models.DateField(blank=True,null=True)
    Transaction_type=models.CharField(max_length=10,blank=True)
    Gross_Amount=models.FloatField(blank=True,null=True)
    Aggregator_Com=models.FloatField(blank=True,null=True)
    Acquirer_Comm=models.FloatField(blank=True,null=True)
    Payable_Merchant=models.FloatField(blank=True)
    Payout_from_Nodal=models.FloatField(blank=True,null=True)
    BankName_Receive_Funds=models.CharField(max_length=50,blank=True,null=True)
    Nodal_Account_No=models.CharField(max_length=50,blank=True,null=True)
    Aggregator_Name=models.CharField(max_length=50,blank=True,null=True)
    Acquirer_Name=models.CharField(max_length=50,blank=True,null=True)
    Refund_Flag=models.CharField(max_length=10,blank=True,null=True)
    Payments_Type=models.CharField(max_length=10,blank=True,null=True)
    MOP_Type=models.CharField(max_length=50,blank=True,null=True)
    Credit_Debit_Date=models.DateField(blank=True,null=True)
    Bank_Name=models.CharField(max_length=15,blank=True,null=True)
    Refund_Order_Id=models.CharField(max_length=50,blank=True,null=True)
    Acq_Id=models.CharField(max_length=125,blank=True,null=True)
    Approve_code=models.CharField(max_length=15,blank=True,null=True)
    Arn_No=models.CharField(max_length=30,blank=True,null=True)
    Card_No=models.CharField(max_length=25,blank=True,null=True)
    Tid=models.CharField(max_length=25,blank=True,null=True)
    Remarks=models.CharField(max_length=50,blank=True,null=True)
    Bank_Ref_id=models.CharField(max_length=25,blank=True,null=True)
    File_upload_Date=models.DateTimeField(blank=True,null=True)
    User_name=models.CharField(max_length=25,blank=True,null=True)
  
    def __str__(self):
        return self.Order_Id


# --------------------------------Ledger Table ---------------------------------------

class Mer_Db_Summary(models.Model): 

   Transaction_Date=models.DateField(blank=True)
   Sale_Amount=models.FloatField(blank=True,null=True)
   Refund_Amount=models.FloatField(blank=True,null=True)
   Trans_Type=models.CharField(max_length=25,blank=True)
   Bank_Id=models.CharField(max_length=25,blank=True)
   Bank_Name=models.CharField(max_length=50,blank=True)
   Sale_No_Txn=models.FloatField(blank=True,null=True)
   Refund_No_Txn=models.FloatField(blank=True,null=True)
   Description=models.CharField(max_length=100,blank=True,null=True)

class Mer_Match_Summary(models.Model): 

   Transaction_Date=models.DateField(blank=True)
   Sale_Amount=models.FloatField(blank=True,null=True)
   Refund_Amount=models.FloatField(blank=True,null=True)
   Trans_Type=models.CharField(max_length=25,blank=True,null=True)
   Bank_Id=models.CharField(max_length=25,blank=True,null=True)
   Bank_Name=models.CharField(max_length=50,blank=True,null=True)
   Actual_Credit_Debit_Date=models.CharField(max_length=15,blank=True,null=True)
   Sale_No_Txn=models.FloatField(blank=True,null=True)
   Refund_No_Txn=models.FloatField(blank=True,null=True)
   Description=models.CharField(max_length=100,blank=True,null=True)

class Nodal_Db_Summary(models.Model): 

   Transaction_Date=models.DateField(blank=True)
   Sale_Amount=models.FloatField(blank=True,null=True)
   Refund_Amount=models.FloatField(blank=True,null=True)
   Trans_Type=models.CharField(max_length=25,blank=True)
   Bank_Name=models.CharField(max_length=50,blank=True)
   Sale_No_Txn=models.FloatField(blank=True,null=True)
   Refund_No_Txn=models.FloatField(blank=True,null=True)
   Description=models.CharField(max_length=100,blank=True,null=True)

class Nodal_Match_Summary(models.Model): 

   Transaction_Date=models.DateField(blank=True)
   Sale_Amount=models.FloatField(blank=True,null=True)
   Refund_Amount=models.FloatField(blank=True,null=True)
   Trans_Type=models.CharField(max_length=25,blank=True,null=True)
   Bank_Name=models.CharField(max_length=50,blank=True,null=True)
   Actual_Credit_Debit_Date=models.CharField(max_length=15,blank=True,null=True)
   Sale_No_Txn=models.FloatField(blank=True,null=True)
   Refund_No_Txn=models.FloatField(blank=True,null=True)
   Description=models.CharField(max_length=100,blank=True,null=True)

#----------------------------------PG ESCALATED QUERIES --------------26 JUN 2024---------------

class Pg_escalated_case(models.Model): 

    Reservation_Id=models.CharField(max_length=50)
    Transaction_Date=models.DateField(blank=True,null=True)
    Transaction_status_code=models.CharField(max_length=50,blank=True,null=True)
    Transaction_status=models.CharField(max_length=50,blank=True,null=True)
    Juspay_flag=models.CharField(max_length=50,blank=True,null=True)
    Booking_Amount=models.CharField(max_length=20,blank=True,null=True)
    Bank_id=models.CharField(max_length=10,blank=True,null=True)
    Bank_name=models.CharField(max_length=50,blank=True,null=True)
    bank_extra_ref1=models.CharField(max_length=50,blank=True,null=True)
    bank_extra_ref2=models.CharField(max_length=50,blank=True,null=True)
    Cancellation_id=models.CharField(max_length=50,blank=True,null=True)
    Refund_Amount=models.CharField(max_length=20,blank=True,null=True)
    Cancellation_Date=models.CharField(max_length=50,blank=True,null=True)
    Actual_Refund_Date=models.CharField(max_length=50,blank=True,null=True)
    Refund_status_code=models.CharField(max_length=50,blank=True,null=True)
    Refund_status=models.CharField(max_length=50,blank=True,null=True)
    Bank_remarks=models.CharField(max_length=500,blank=True,null=True)
    Complaint_Received_Date=models.DateField()
    Complaint_received_from=models.CharField(max_length=50,blank=True,null=True)
    Email_id=models.CharField(max_length=50,blank=True,null=True)
    Complaint_Nature=models.CharField(max_length=100,blank=True,null=True)
    Card_issue_bank=models.CharField(max_length=50,blank=True,null=True)
    problem_at_whom=models.CharField(max_length=50,blank=True,null=True)
    Email_subject=models.CharField(max_length=150,blank=True,null=True)
    Complaint_type=models.CharField(max_length=50,blank=True,null=True)
    Complaint_rcvd_by=models.CharField(max_length=50,blank=True,null=True)
    Complaint_updated_by=models.CharField(max_length=50,blank=True,null=True)
    Complaint_Update_Date=models.DateField(blank=True,null=True)
    Forward_department=models.CharField(max_length=50,blank=True,null=True)
    Forwarded_date=models.DateField(blank=True,null=True)
    Esclation_rcvd_dept=models.CharField(max_length=50,blank=True,null=True)
    Bank_Comuni_Date=models.DateField(blank=True,null=True)
    Bank_communi_update_by=models.CharField(max_length=50,blank=True,null=True)
    Bank_communi_update_on=models.DateField(blank=True,null=True)
    Bank_rcvd_Date=models.DateField(blank=True,null=True)
    Bank_Response=models.CharField(max_length=300,blank=True,null=True)
    Bank_Res_update_by=models.CharField(max_length=50,blank=True,null=True)
    Bank_Res_update_on=models.DateField(blank=True,null=True)
    Response_customer_Date=models.DateField(blank=True,null=True)
    Response_customer_thro=models.CharField(max_length=50,blank=True,null=True)
    Response_customer_update_by=models.CharField(max_length=50,blank=True,null=True)
    Response_customer_update_on=models.DateField(blank=True,null=True)
    Received_letter_no=models.CharField(max_length=50,blank=True,null=True)
    Reopen_by=models.CharField(max_length=50,blank=True,null=True)
    Reopen_Date=models.DateField(blank=True,null=True)
    Reopen_Reason=models.CharField(max_length=50,blank=True,null=True)
    Reopen_by=models.CharField(max_length=50,blank=True,null=True)
    Reopen_second_by=models.CharField(max_length=50,blank=True,null=True)
    Reopen_second_Date=models.DateField(blank=True,null=True)
    Reopen_second_Reason=models.CharField(max_length=50,blank=True,null=True)
    penality_eligible=models.CharField(max_length=50,blank=True,null=True)
    penality_update_date=models.DateField(blank=True,null=True)
    other_updated_by=models.CharField(max_length=50,blank=True,null=True)
    complaint_status=models.CharField(max_length=100,blank=True,null=True)
    Remarks1=models.CharField(max_length=500,blank=True,null=True)
    Remarks2=models.CharField(max_length=500,blank=True,null=True)
    Account_closed_file=models.CharField(max_length=150,blank=True,null=True)
    Complaint_recorded_Date=models.DateField(blank=True,null=True)
    Complaint_department=models.CharField(max_length=50,blank=True,null=True)
    Bank_actual_refund_Date=models.DateField(blank=True,null=True)
    User_department=models.CharField(max_length=25,blank=True,null=True)
    Pnr_Number=models.CharField(max_length=15,blank=True,null=True)
    other_updated_Date=models.DateField(blank=True,null=True)
    Account_closed_date=models.DateField(blank=True,null=True)

#----------------------------------TDR QUERIES --------------03 JULY 2024---------------

class tdr_payorder_received_details(models.Model):

    Zonal_Railway=models.CharField(max_length=50,blank=True,null=True)
    neft_detail=models.CharField(max_length=300,blank=True,null=True)
    Letter_Date=models.DateField(blank=True,null=True)
    Payorder_Received_Date=models.DateField(blank=True,null=True)
    Statement_Amount=models.FloatField(blank=True,null=True)
    No_of_PNR=models.CharField(max_length=4,blank=True,null=True)
    Payorder_Number=models.CharField(max_length=8,blank=True,null=True)
    Payorder_Date=models.DateField(blank=True,null=True)
    Payorder_Amount=models.FloatField(blank=True,null=True)
    Co_details=models.CharField(max_length=100,blank=True,null=True)
    Remarks=models.CharField(max_length=200,blank=True,null=True)
    Neft_Received_Date=models.DateField(blank=True,null=True)
    Neft_Amount=models.FloatField(blank=True,null=True)
    user_name=models.CharField(max_length=25,blank=True,null=True)
    Update_Date=models.DateField(blank=True,null=True)
    Asign_to=models.CharField(max_length=25,blank=True,null=True)
    Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Recon_Remarks=models.CharField(max_length=200,blank=True,null=True)
    Statement_Number=models.CharField(max_length=300,blank=True,null=True)

    
#----------------------------METRO TABLE 06 AUG 2024-----------------------------------

class metro_payment_details(models.Model):
    Transaction_Date=models.DateField(unique=True)
    Booking_Count=models.FloatField(blank=True,null=True)
    Booking_Amount=models.FloatField(blank=True,null=True)
    Refund_Count=models.FloatField(blank=True,null=True)
    Refund_Amount=models.FloatField(blank=True,null=True)
    Net_Amount=models.FloatField(blank=True,null=True)
    Settled_Date=models.DateField(blank=True,null=True)
    Actual_Credit_Date=models.DateField(blank=True,null=True)
    Actual_Credit_Amount=models.FloatField(blank=True,null=True)
    Utr_Number=models.CharField(max_length=100,blank=True,null=True)
    Amount_Adjusted=models.FloatField(blank=True,null=True)
    Adjusted_Narration=models.CharField(max_length=200,blank=True,null=True)
    Adjusted_Date=models.DateField(blank=True,null=True)
    Remarks=models.CharField(max_length=200,blank=True,null=True)
    File_upload_date=models.DateField(blank=True,null=True)
    Payment_updated_by=models.CharField(max_length=50,blank=True,null=True)
    Adjustment_updated_by=models.CharField(max_length=50,blank=True,null=True)
    File_upload_by=models.CharField(max_length=50,blank=True,null=True)
    Payment_updated_date=models.DateField(blank=True,null=True)
    Adjustment_updated_date=models.DateField(blank=True,null=True) 
    Metro_Name=models.CharField(max_length=50,blank=True,null=True)  
    

class metro_sale_details(models.Model):
    Transaction_Id=models.CharField(max_length=50,blank=True,null=True)
    Activation_date=models.DateField(blank=True,null=True)
    Ticket_Amount=models.FloatField(blank=True,null=True)
    Refund_Amount=models.FloatField(blank=True,null=True)
    Metro_psgn_Id=models.CharField(unique=True,max_length=50)
    Metro_Qr_Ticket_No=models.CharField(unique=True,max_length=50)
    Metro_Psgn_Serial_Number=models.CharField(max_length=10,blank=True,null=True)
    Cancellation_Id=models.CharField(max_length=50,blank=True,null=True)
    Cancellation_Date=models.DateField(blank=True,null=True)
    Cancel_Status=models.CharField(max_length=25,blank=True,null=True)
    Payment_Cash_Id=models.CharField(max_length=50,blank=True,null=True)
    Entiry_Code=models.CharField(max_length=50,blank=True,null=True)
    Bank_Id=models.CharField(max_length=25,blank=True,null=True)
    Bank_Name=models.CharField(max_length=50,blank=True,null=True)
    Bank_Transaction_Number=models.CharField(max_length=100,blank=True,null=True)
    Transaction_Status=models.CharField(max_length=25,blank=True,null=True)
    Payment_Date=models.DateField(blank=True,null=True)
    Transaction_Date=models.DateField(blank=True,null=True)
    Reservation_Id=models.CharField(max_length=25,blank=True,null=True)
    Pnr_Number=models.CharField(max_length=25,blank=True,null=True)
    Service_Status=models.CharField(max_length=25,blank=True,null=True)
    Service_Type=models.CharField(max_length=25,blank=True,null=True)
    Actual_Payment_Date=models.DateField(blank=True,null=True)
    Actula_Payment_Status=models.CharField(max_length=25,blank=True,null=True)
    Utr_Number=models.CharField(max_length=50,blank=True,null=True)
    Metro_Id=models.CharField(max_length=25,blank=True,null=True)
    Metro_Name=models.CharField(max_length=50,blank=True,null=True)
    Update_Date=models.DateField(blank=True,null=True)
    Update_user_name=models.CharField(max_length=25,blank=True,null=True)
    Payment_Update_Date=models.DateField(blank=True,null=True)
    Payment_update_user=models.CharField(max_length=25,blank=True,null=True)
    Remarks=models.CharField(max_length=150,blank=True,null=True)

class metro_refund_details(models.Model):

    Transaction_Id=models.CharField(max_length=50,blank=True,null=True)
    Activation_date=models.DateField(blank=True,null=True)
    Ticket_Amount=models.FloatField(blank=True,null=True)
    Refund_Amount=models.FloatField(blank=True,null=True)
    Metro_psgn_Id=models.CharField(unique=True,max_length=50)
    Metro_Qr_Ticket_No=models.CharField(unique=True,max_length=50)
    Metro_Psgn_Serial_Number=models.CharField(max_length=25,blank=True,null=True)
    Metro_Cancel_Status=models.CharField(max_length=25,blank=True,null=True)
    Irctc_Cancellation_Date=models.DateField(blank=True,null=True)
    Irctc_Cancellation_Id=models.CharField(max_length=25,blank=True,null=True)
    Irctc_Reservation_Id=models.CharField(max_length=25,blank=True,null=True)
    Refund_Status=models.CharField(max_length=25,blank=True,null=True)
    Irctc_Cancellation_Status=models.CharField(max_length=25,blank=True,null=True)
    Cancellation_Type=models.CharField(max_length=25,blank=True,null=True)
    No_Of_Passengers=models.CharField(max_length=25,blank=True,null=True)
    Created_Date=models.DateField(blank=True,null=True)
    Prs_Reservation_Id=models.CharField(max_length=50,blank=True,null=True)
    Pnr_Number=models.CharField(max_length=25,blank=True,null=True)
    Service_Status=models.CharField(max_length=25,blank=True,null=True)
    Service_Type=models.CharField(max_length=25,blank=True,null=True)
    Actual_Payment_Date=models.DateField(blank=True,null=True)
    Actula_Payment_Status=models.CharField(max_length=25,blank=True,null=True)
    Utr_Number=models.CharField(max_length=50,blank=True,null=True)
    Metro_Id=models.CharField(max_length=25,blank=True,null=True)
    Metro_Name=models.CharField(max_length=25,blank=True,null=True)
    Update_Date=models.DateField(blank=True,null=True)
    Update_user_name=models.CharField(max_length=25,blank=True,null=True)
    Payment_Update_Date=models.DateField(blank=True,null=True)
    Payment_update_user=models.CharField(max_length=25,blank=True,null=True)
    Remarks=models.CharField(max_length=150,blank=True,null=True)
    
class bob_mer_net_bank_stement(models.Model):
    
    Reference_Id=models.CharField(unique=True,max_length=25)
    Transaction_Date=models.DateField(blank=True,null=True)
    Description=models.CharField(max_length=250,blank=True,null=True)
    Debit_Amount=models.FloatField(blank=True,null=True)
    Credit_Amount=models.FloatField(blank=True,null=True)
    Balance_Amount=models.FloatField(blank=True,null=True)
    Remarks=models.CharField(max_length=25,blank=True,null=True)

class bob_mer_mpr_bank_record(models.Model):
    
    Reference_Id=models.CharField(unique=True,max_length=25)
    Transaction_Date=models.DateField(blank=True,null=True)
    Transaction_Id=models.CharField(max_length=50,blank=True,null=True)
    Bank_Ref_Id=models.CharField(max_length=50,blank=True,null=True)
    Transaction_Type=models.CharField(max_length=25,blank=True,null=True)
    Net_Amount=models.FloatField(blank=True,null=True)
    Bank_id=models.CharField(max_length=25,blank=True,null=True)
    Bank_Name=models.CharField(max_length=25,blank=True,null=True)
    Remarks=models.CharField(max_length=25,blank=True,null=True)
    Description=models.CharField(max_length=250,blank=True,null=True)
    Recon_Status=models.CharField(max_length=25,blank=True,null=True)
    Recon_Remarks=models.CharField(max_length=100,blank=True,null=True)



    
   
    
						

  