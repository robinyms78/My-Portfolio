//
//  LoginModel.m
//  Login
//
//  Created by Mok Hei Chee on 5/19/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "LoginModel.h"


@implementation LoginModel

-(BOOL)verifyUser:(NSString *)userID andPassword:(NSString *)password {
	//if([userID isEqualToString:password]) {
	if([userID isEqualToString:@"admin"]) {
		if([password isEqualToString:@"admin"]) {
			return TRUE;
		} else {
			return FALSE;
		}
	} else {
		if([userID isEqualToString:@"student"]) {
			if([password isEqualToString:@"student"]) {
				return TRUE;
			} else {
				return FALSE;
			}
		}
    }
	return FALSE;
}
@end
