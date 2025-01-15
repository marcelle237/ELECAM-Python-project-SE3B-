export const config = {
  initialMessages: [
    {
      text: "Hello! How can I assist you with voting?",
      sender: "bot",
    },
  ],
  customStyles: {
    botMessageBox: {
      backgroundColor: "#4caf50",
    },
    chatButton: {
      backgroundColor: "#4caf50",
    },
  },
  customComponents: {
    // Customize user message component here
    userAvatar: () => null,  // This hides the avatar/icon
  },
};
