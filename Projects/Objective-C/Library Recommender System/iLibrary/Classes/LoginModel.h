//
//  LoginModel.h
//  Login
//
//  Created by Mok Hei Chee on 5/19/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>


@interface LoginModel : NSObject {

}

- (BOOL) verifyUser:(NSString *)userID andPassword:(NSString *)password;

@end
