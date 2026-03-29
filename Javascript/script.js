
const saudacao = (nome) => `Olá, ${nome}!`;

test('deve retornar a saudação correta', () => {
  const resultado = saudacao('Alice');
  
  expect(resultado).toBe('Olá, Alice!');
});