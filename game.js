import React, { useState } from 'react';
function Square({ value, onSquareClick })
{
  return (
    <button className="square" onClick={onSquareClick} style={squareStyle}>
      {value}
    </button>
  );
}
export default function Game()
{
  const [squares, setSquares] = useState(Array(9).fill(null));
  const [xIsNext, setXIsNext] = useState(true);
  const winner = calculateWinner(squares);
  const isDraw = !winner && squares.every(sq => sq !== null);
  function handleClick(i) 
  {
    if (squares[i] || winner) return;
    const nextSquares = squares.slice();
    nextSquares[i] = xIsNext ? "X" : "O";
    setSquares(nextSquares);
    setXIsNext(!xIsNext);
  }
  const status = winner 
    ? `Winner: ${winner}` 
    : isDraw 
    ? "It's a Draw!" 
    : `Next Player: ${xIsNext ? "X" : "O"}`;
  return (
    <div className="game" style={{ textAlign: 'center', marginTop: '50px' }}>
      <div className="status" style={{ marginBottom: '10px', fontWeight: 'bold' }}>{status}</div>
      <div style={boardStyle}>
        {squares.map((val, idx) => (
          <Square key={idx} value={val} onSquareClick={() => handleClick(idx)} />
        ))}
      </div>
      <button onClick={() => setSquares(Array(9).fill(null))} style={resetStyle}>
        Reset Game
      </button>
    </div>
  );
}
function calculateWinner(squares) 
{
  const lines = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]            
  ];
  for (let [a, b, c] of lines)
  {
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) 
    {
      return squares[a];
    }
  }
  return null;
}
const boardStyle =
{
  display: 'grid',
  gridTemplateColumns: 'repeat(3, 100px)',
  justifyContent: 'center',
  gap: '5px'
};
const squareStyle =
{
  width: '100px',
  height: '100px',
  fontSize: '24px',
  cursor: 'pointer'
};
const resetStyle = 
{
  marginTop: '20px',
  padding: '10px 20px',
  cursor: 'pointer'
};