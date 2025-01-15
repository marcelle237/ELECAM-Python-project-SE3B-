import React, { useState } from 'react';

export const EligibilityForm = () => {
  const [age, setAge] = useState('');
  const [nationality, setNationality] = useState('');
  const [isEligible, setIsEligible] = useState(null);

  const checkEligibility = () => {
    if (age >= 18 && nationality === 'Cameroonian') {
      setIsEligible(true);
    } else {
      setIsEligible(false);
    }
  };

  return (
    <div className="eligibility-form">
      <h2>Check Voting Eligibility</h2>
      <label>
        Age:
        <input
          type="number"
          value={age}
          onChange={(e) => setAge(e.target.value)}
        />
      </label>
      <br />
      <label>
        Nationality:
        <input
          type="text"
          value={nationality}
          onChange={(e) => setNationality(e.target.value)}
        />
      </label>
      <br />
      <button onClick={checkEligibility}>Check Eligibility</button>

      {isEligible !== null && (
        <div>
          {isEligible ? <p>You are eligible to vote!</p> : <p>You are not eligible to vote.</p>}
        </div>
      )}
    </div>
  );
};
