   /*******************************************************/
   /*      "C" Language Integrated Production System      */
   /*                                                     */
   /*             CLIPS Version 6.24  06/05/06            */
   /*                                                     */
   /*          MISCELLANEOUS FUNCTIONS HEADER FILE        */
   /*******************************************************/

/*************************************************************/
/* Purpose:                                                  */
/*                                                           */
/* Principal Programmer(s):                                  */
/*      Gary D. Riley                                        */
/*                                                           */
/* Contributing Programmer(s):                               */
/*                                                           */
/* Revision History:                                         */
/*      6.23: Corrected compilation errors for files         */
/*            generated by constructs-to-c. DR0861           */
/*                                                           */
/*      6.24: Renamed BOOLEAN macro type to intBool.         */
/*                                                           */
/*************************************************************/

#ifndef _H_miscfun

#define _H_miscfun

#ifdef LOCALE
#undef LOCALE
#endif

#ifdef _MISCFUN_SOURCE_
#define LOCALE
#else
#define LOCALE extern
#endif

   LOCALE void                           MiscFunctionDefinitions(void *);
   LOCALE void                           CreateFunction(void *,DATA_OBJECT_PTR);
   LOCALE long long                      SetgenFunction(void *);
   LOCALE void                          *GensymFunction(void *);
   LOCALE void                          *GensymStarFunction(void *);
   LOCALE long long                      RandomFunction(void *);
   LOCALE void                           SeedFunction(void *);
   LOCALE long long                      LengthFunction(void *);
   LOCALE void                           ConserveMemCommand(void *);
   LOCALE long long                      ReleaseMemCommand(void *);
   LOCALE long long                      MemUsedCommand(void *);
   LOCALE long long                      MemRequestsCommand(void *);
   LOCALE void                           OptionsCommand(void *);
   LOCALE void                           ExpandFuncCall(void *,DATA_OBJECT *);
   LOCALE void                           DummyExpandFuncMultifield(void *,DATA_OBJECT *);
   LOCALE void                          *CauseEvaluationError(void *);
   LOCALE intBool                        SetSORCommand(void *);
   LOCALE void                          *GetFunctionRestrictions(void *);
   LOCALE void                           AproposCommand(void *);
   LOCALE void                          *GensymStar(void *);
   LOCALE void                           GetFunctionListFunction(void *,DATA_OBJECT *);
   LOCALE void                           FuncallFunction(void *,DATA_OBJECT *);
   LOCALE void                           NewFunction(void *,DATA_OBJECT *);
   LOCALE void                           CallFunction(void *,DATA_OBJECT *);
   LOCALE double                         TimerFunction(void *);
   LOCALE double                         TimeFunction(void *);

#endif






