
@interface IFChargeRequest : NSObject
{
@private
    NSObject* _delegate;

    NSString* _returnAppName;
    NSString* _returnURL;

    NSString* _address;
    NSString* _amount;
    NSString* _city;
    NSString* _company;
    NSString* _country;
    NSString* _currency;
    NSString* _description;
    NSString* _email;
    NSString* _firstName;
    NSString* _invoiceNumber;
    NSString* _lastName;
    NSString* _phone;
    NSString* _state;
    NSString* _zip;
}

@property (assign) NSObject* delegate;
@property (copy) NSString* returnAppName;
@property (copy) NSString* returnURL;
- (void)setReturnURL:(NSString*)url withExtraParams:(NSDictionary*)extraParams;

@property (copy) NSString* address;

@property (copy) NSString* amount;

@property (copy) NSString* city;

@property (copy) NSString* company;

@property (copy) NSString* country;

@property (copy) NSString* currency;

@property (copy) NSString* description;


@property (copy) NSString* email;


@property (copy) NSString* firstName;

@property (copy) NSString* invoiceNumber;


@property (copy) NSString* lastName;

@property (copy) NSString* phone;


@property (copy) NSString* state;


@property (copy) NSString* zip;

+ (NSArray*)knownFields;


- init;

- initWithDelegate:(NSObject*)delegate;


- (NSURL*)requestURL;

#if TARGET_OS_IPHONE


- (void)submit;

#endif

@end

@interface NSObject (IFChargeRequestDelegate)


- (void)creditCardTerminalNotInstalled;

@end

#define IF_CHARGE_API_VERSION  @"1.0.0"
#define IF_CHARGE_API_BASE_URI @"com-innerfence-ccterminal://charge/" IF_CHARGE_API_VERSION @"/"

#define IF_CHARGE_NONCE_KEY @"ifcc_request_nonce"


#define IF_CHARGE_NOT_INSTALLED_BUTTON  ( NSLocalizedString( @"OK", nil ) )
#define IF_CHARGE_NOT_INSTALLED_MESSAGE ( NSLocalizedString( \
    @"Install Credit Card Terminal to enable this functionality.", nil \
) )
#define IF_CHARGE_NOT_INSTALLED_TITLE   ( NSLocalizedString( @"Unable to Charge", nil ) )
