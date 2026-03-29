
INSERT INTO usuarios (nome, email) VALUES ('Teste Unitario', 'teste@email.com');

SELECT 
    CASE 
        WHEN COUNT(*) > 0 THEN 'PASSOU: Usuário encontrado'
        ELSE 'FALHOU: Usuário não inserido'
    END AS status_teste
FROM usuarios 
WHERE email = 'teste@email.com';

DELETE FROM usuarios WHERE email = 'teste@email.com';