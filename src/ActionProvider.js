class ActionProvider {
    constructor(createChatBotMessage, setStateFunc) {
      this.createChatBotMessage = createChatBotMessage;
      this.setState = setStateFunc;
    }
  
    handleVoteQuery() {
      const message = this.createChatBotMessage("You can vote at any ELECAM office.");
      this.setState((prev) => ({
        ...prev,
        messages: [...prev.messages, message],
      }));
    }
  
    handleEligibilityQuery() {
      const message = this.createChatBotMessage("Check if you are eligible based on age and nationality.");
      this.setState((prev) => ({
        ...prev,
        messages: [...prev.messages, message],
      }));
    }
  }
  
  export default ActionProvider;
  