import websockets
import asyncio

import cv2, base64

port = 8080
print("Listening on port :", port)

async def transmit (websocket, path):
  print("Client connected.")
  try:
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
      _, frame = cap.read()

      frame = cv2.flip(frame, 0)
      frame = cv2.flip(frame, 1)
      
      encoded = cv2.imencode('.jpg', frame)[1]

      data = str(base64.b64encode(encoded))
      data = data[2:len(data)-1]
      
      await websocket.send(data)

      #cv2.imshow("Video feed", frame)
      #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

    cap.release()

  except websockets.connection.ConnectionClosed as e:
    print("Client disconnected.")
    cap.release()
  except:
    print("Unexpected error occurred.")

start_server = websockets.serve(transmit, port=port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

cap.release()
