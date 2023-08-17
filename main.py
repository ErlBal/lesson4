class SavingAccount: ...


class CheckingAccount: ...


class Stock: ...


class Bond: ...


class RealEstate: ...


class BankAccount(SavingAccount, CheckingAccount): ...


class Security(Stock, Bond): ...


class InaurableItem(BankAccount, RealEstate): ...


class Asset(BankAccount, RealEstate, Security): ...


class InterestBearingItem(Security, BankAccount): ...

print(BankAccount.mro())

print(Security.mro())

print(InaurableItem.mro())

print(Asset.mro())

print(InterestBearingItem.mro())