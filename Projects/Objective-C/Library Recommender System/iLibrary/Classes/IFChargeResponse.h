
#define IF_CHARGE_RESPONSE_FIELD_PREFIX @"ifcc_"

typedef enum {
   
 kIFChargeResponseCodeApproved,
 kIFChargeResponseCodeCancelled,

 kIFChargeResponseCodeDeclined,

  kIFChargeResponseCodeError
} IFChargeResponseCode;

@interface IFChargeResponse : NSObject
{
@private
    NSString*            _baseURL;
    NSString*            _amount;
    NSString*            _cardType;
    NSString*            _currency;
    NSDictionary*        _extraParams;
    NSString*            _redactedCardNumber;
    IFChargeResponseCode _responseCode;
    NSString*            _responseType;
}


@property (readonly,copy)   NSString*            amount;

@property (readonly,copy)   NSString*            cardType;


@property (readonly,copy)   NSString*            currency;


@property (readonly,retain) NSDictionary*        extraParams;


@property (readonly,copy)   NSString*            redactedCardNumber;


@property (readonly,assign) IFChargeResponseCode responseCode;


- initWithURL:(NSURL*)url;

+ (NSArray*)knownFields;
+ (NSDictionary*)responseCodeMapping;

@end
