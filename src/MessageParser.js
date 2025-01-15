class MessageParser {
    constructor(actionProvider) {
      this.actionProvider = actionProvider;
    }
  
    parse(message) {
      if (message.includes("vote")) {
        this.actionProvider.handleVoteQuery();
      } else if (message.includes("eligibility")) {
        this.actionProvider.handleEligibilityQuery();
      }
    }
  }
  
  export default MessageParser;
  
