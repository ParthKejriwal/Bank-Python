class Atm(object):   
    def __init__(self, atmCardNo, pinNo):
        self.atmCardNo = atmCardNo
        self.pinNo = pinNo
        
    def cashWithdrawl(self,atmCardNo):
        print(atmCardNo)

    def balanceEnquiry(self, pinNo, atmCardNo):
        print(pinNo)

    def cashDeposition(atmCardNo):
        print(atmCardNo)

withdraw= Atm(9001,1001)
enquire= Atm(1000,2000)

print(withdraw.atmCardNo)
print(enquire.pinNo)