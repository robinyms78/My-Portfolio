#ifndef SRI_TCP_UTILS_H
#define SRI_TCP_UTILS_H

#include "Poco/Net/StreamSocket.h"
#include "Poco/Exception.h"
#include "SRI/SRIUtil/SRIString.h"
#include "SRI/SRIGlobals.h"
#include "SRI/SRIUtil/SRIRef.h"

namespace SRI {

/// Class containing utility methods for communicating over TCP ports
	class SRITCPUtils {
	public:
		/** Reads socket and returns string containing stuff read.
		 * Blocks until full message is received
		 */
		static int szReadSocket(Poco::Net::StreamSocket* socket, Ref<SRI::String> msg) {
			int msgSize;
			int ret = vReceiveNBytes((char *)(&msgSize), sizeof(int), socket);

			if (ret <= 0) return SRI_ERR_NETWORK;
	
			char *msgBuf = new char[msgSize + 1]; //+1 for appending '\0' 
			ret = vReceiveNBytes(msgBuf, msgSize, socket);

			if (ret <= 0) return SRI_ERR_NETWORK;

			msgBuf[msgSize] = '\0'; //append null char

			msg.ptGetObj()->append(msgBuf);
			delete[] msgBuf;

			return SRI_OK;
		}

		/** Sends msg over socket.
		*/
		static int vSendSocket(SRI::String msg, Poco::Net::StreamSocket* socket) {
			int size = msg.size(); 
			vSendNBytes((char *)&size, sizeof(int), socket);

			return vSendNBytes(const_cast<char *>(msg.c_str()), size, socket);

		}

	private:
		static int vReceiveNBytes(char *buf, int len, Poco::Net::StreamSocket* sock) {
			char *startPos = buf;
			int iniLen = len;
			while (len > 0) {
				try {
					
					int rcv = sock->receiveBytes(startPos, len); 
					if (rcv == 0) return SRI_ERR_NETWORK;
					//according to poco documentation, if ret val is 0 that means graceful shutdown, i.e. connection aborted
					//TODO: handle negative ret vals?
					//TODO: handle timeout?
					len -= rcv;
					startPos += rcv;
				}
				catch (Poco::Exception& e) {
					SRI::String ename(e.className());
					if (ename == "class Poco::ConnectionAbortedException") {
						return SRI_ERR_NETWORK;
					}
					else return SRI_ERR;
					
				}

				
			}
			return iniLen;
		}


		static int vSendNBytes(char *buf, int len, Poco::Net::StreamSocket* sock) {
			int iniLen = len;
			while (len > 0) {
				try {
					int sent = sock->sendBytes(buf, len); //TODO: handle negative ret vals?
					len -= sent;
					buf += sent;
				}
				catch (Poco::Exception& e) {
					SRI::String ename(e.className());
					if (ename == "class Poco::ConnectionAbortedException") {
						return SRI_ERR_NETWORK;
					}
					return SRI_ERR;
				}
				
			}
			return iniLen;
		}

	};

} //end namespace SRI

#endif SRI_TCP_UTILS_H