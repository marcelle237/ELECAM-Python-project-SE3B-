import React, { useState } from "react";
import "./App.css";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { Chatbot } from "react-chatbot-kit";
import { config } from "./chatbotConfig";
import MessageParser from "./MessageParser";
import ActionProvider from "./ActionProvider";
import { EligibilityForm } from "./EligibilityForm";

const App = () => {
  const [showEligibilityForm, setShowEligibilityForm] = useState(false);

  const offices = [
    { id: 1, name: "ELECAM Office 1", lat: 4.5, lng: 11.5, address: "Address 1" },
    { id: 2, name: "ELECAM Office 2", lat: 4.7, lng: 11.6, address: "Address 2" },
  ];

  return (
    <div className="App">
      <header>
        <h1>Welcome to Your voting  ELECAM Information System   Assistant</h1>
        <button onClick={() => setShowEligibilityForm(!showEligibilityForm)}>
          Check Voting Eligibility
        </button>

    
      </header>

      {showEligibilityForm ? (
        <EligibilityForm />
      ) : (
        <>
          <MapContainer center={[4.5, 11.5]} zoom={10} style={{ height: "400px", width: "100%" }}>
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            {offices.map((office) => (
              <Marker key={office.id} position={[office.lat, office.lng]}>
                <Popup>
                  <h3>{office.name}</h3>
                  <p>{office.address}</p>
                </Popup>
              </Marker>
            ))}
          </MapContainer>

          <Chatbot
            config={config}
            messageParser={MessageParser}
            actionProvider={ActionProvider}
          />
        </>
      )}
    </div>
  );
};

export default App;
