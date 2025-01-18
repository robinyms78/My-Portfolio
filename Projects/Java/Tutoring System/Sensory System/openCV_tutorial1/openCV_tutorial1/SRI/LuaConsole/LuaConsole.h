#ifndef LUA_CONSOLE_H
#define LUA_CONSOLE_H
#include "SRI/SRIEngine/SRIPlugin.h"
#include "SRI/SRI.h"
#include "SRI/SRIEngine/ReactiveComponent.h"
#include "iup.h"


namespace SRI{

//INST_TEMPLATE SRI::List<SRI::String>;
//INST_TEMPLATE SRI::ListIterator<SRI::String>;

class SRI_PLUGIN_API LuaConsole: public ReactiveComponent{

private:
	Logger m_tLog;

	Ihandle* m_ptQuitBut;
	Ihandle* m_ptSendBut;
	Ihandle* m_ptMainBox;
	Ihandle* m_ptTextInput;

	Ihandle* m_ptDlg;
	bool m_bGuiIsClosed;
	bool m_bIsMasterConsole;

	static int dlgClose_cb(Ihandle* dlg);
	static int sendBut_cb(Ihandle* self);
	static int keyEnter_cb(Ihandle* self, int key);

	OutputPort* m_ptCommandOutput; 

	//SRI::List<SRI::String> m_lCommandHistory;
	//SRI::ListIterator<SRI::String> m_tHistoryPointer;

public:
	LuaConsole(SRI::String name);
	virtual ~LuaConsole();
	void vSetGuiIsClosed();

	void vSendScript();
	void vKeyEntered(int key);

	void vInit();
	void vStep();
	bool bHasMoreSteps();

	/** If the console is master, then it issues a close enginge command when the Gui is closed*/
	void vSetMasterConsole(bool isMaster);
};

}// end namespace


#endif