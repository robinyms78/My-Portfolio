//
//  ReaderSampleViewController.h
//  ReaderSample
//
//  Created by spadix on 8/4/10.
//

#import <UIKit/UIKit.h>

@interface ReaderSampleViewController
    : UIViewController 
    // ADD: delegate protocol
    < ZBarReaderDelegate >
{
    UIImageView *resultImage;
    UITextView *resultText;
	NSMutableArray *booksModel;
}
@property(nonatomic,retain)NSMutableArray *booksModel;
@property (nonatomic, retain) IBOutlet UIImageView *resultImage;
@property (nonatomic, retain) IBOutlet UITextView *resultText;
- (IBAction) scanButtonTapped;
@end
