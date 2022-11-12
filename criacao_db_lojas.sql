CREATE database db_loja;

USE db_loja;

CREATE TABLE `tb_estado`
(
 `id_estado`  int NOT NULL AUTO_INCREMENT ,
 `nm_estado`  varchar(50) NOT NULL ,
 `sgl_estado` varchar(2) NOT NULL ,

PRIMARY KEY (`id_estado`),
UNIQUE KEY `uk_nm` (`nm_estado`),
UNIQUE KEY `uk_sgl` (`sgl_estado`)
);

CREATE TABLE `tb_cidade`
(
 `id_cidade` int NOT NULL AUTO_INCREMENT ,
 `nm_cidade` varchar(100) NOT NULL ,
 `cd_estado` int NOT NULL ,

PRIMARY KEY (`id_cidade`),
KEY `FK_2` (`cd_estado`),
CONSTRAINT `FK_2` FOREIGN KEY `FK_2` (`cd_estado`) REFERENCES `tb_estado` (`id_estado`)
);

CREATE TABLE `tb_bairro`
(
 `id_bairro` int NOT NULL AUTO_INCREMENT ,
 `nm_bairro` varchar(50) NOT NULL ,
 `cd_cidade` int NOT NULL ,

PRIMARY KEY (`id_bairro`),
KEY `FK_2` (`cd_cidade`),
CONSTRAINT `FK_3` FOREIGN KEY `FK_2` (`cd_cidade`) REFERENCES `tb_cidade` (`id_cidade`)
);

CREATE TABLE `tb_endereco`
(
 `id_endereco`  int NOT NULL AUTO_INCREMENT ,
 `cep_endereco` varchar(10) NOT NULL ,
 `cd_bairro`    int NOT NULL ,
 `nm_endereco`  varchar(50) NOT NULL ,
 `num_endereco` varchar(10) NOT NULL ,
 `des_endereco` varchar(100) NOT NULL ,

PRIMARY KEY (`id_endereco`),
KEY `FK_2` (`cd_bairro`),
CONSTRAINT `FK_4` FOREIGN KEY `FK_2` (`cd_bairro`) REFERENCES `tb_bairro` (`id_bairro`)
);

CREATE TABLE `tb_sexo`
(
 `id_sexo` int NOT NULL AUTO_INCREMENT ,
 `nm_sexo` varchar(10) NOT NULL ,

PRIMARY KEY (`id_sexo`),
UNIQUE KEY `uk_nm` (`nm_sexo`)
);

CREATE TABLE `tb_usuario`
(
 `id_usuario`      int NOT NULL AUTO_INCREMENT ,
 `nm_usuario`      varchar(100) NOT NULL ,
 `cd_sexo`         int NOT NULL ,
 `cpf_usuario`     varchar(15) NOT NULL ,
 `email_usuario`   varchar(50) NOT NULL ,
 `senha_usuario`   varchar(16) NOT NULL ,
 `tel_usuario`     varchar(15) NOT NULL ,
 `dt_nasc_usuario` date NOT NULL ,
 `agencia_usuario` varchar(6) NULL ,
 `conta_usuario`   varchar(15) NULL ,
 `banco_usuario`   integer NULL ,

PRIMARY KEY (`id_usuario`),
UNIQUE KEY `uk_agencia_conta_banco` (`conta_usuario`, `agencia_usuario`, `banco_usuario`),
UNIQUE KEY `uk_cpf` (`cpf_usuario`),
UNIQUE KEY `uk_email` (`email_usuario`),
UNIQUE KEY `uk_tel` (`tel_usuario`),
KEY `FK_5` (`cd_sexo`),
CONSTRAINT `FK_1` FOREIGN KEY `FK_5` (`cd_sexo`) REFERENCES `tb_sexo` (`id_sexo`)
);

CREATE TABLE `tb_endereco__usuario`
(
 `id_endereco_usuario` int NOT NULL AUTO_INCREMENT ,
 `cd_endereco`         int NOT NULL ,
 `cd_usuario`          int NOT NULL ,

PRIMARY KEY (`id_endereco_usuario`),
KEY `FK_2` (`cd_endereco`),
CONSTRAINT `FK_5` FOREIGN KEY `FK_2` (`cd_endereco`) REFERENCES `tb_endereco` (`id_endereco`),
KEY `FK_3` (`cd_usuario`),
CONSTRAINT `FK_6` FOREIGN KEY `FK_3` (`cd_usuario`) REFERENCES `tb_usuario` (`id_usuario`)
);

CREATE TABLE `tb_cartao`
(
 `id_cartao`  int NOT NULL AUTO_INCREMENT ,
 `nm_cartao`  varchar(50) NOT NULL ,
 `num_cartao` varchar(16) NOT NULL ,
 `val_cartao` date NOT NULL ,
 `ban_cartao` varchar(30) NOT NULL ,

PRIMARY KEY (`id_cartao`)
);

CREATE TABLE `tb_cartao_usuario`
(
 `id_cartao_usuario` int NOT NULL AUTO_INCREMENT ,
 `id_usuario`        int NOT NULL ,
 `id_cartao`         int NOT NULL ,

PRIMARY KEY (`id_cartao_usuario`),
KEY `FK_2` (`id_usuario`),
CONSTRAINT `FK_7` FOREIGN KEY `FK_2` (`id_usuario`) REFERENCES `tb_usuario` (`id_usuario`),
KEY `FK_3` (`id_cartao`),
CONSTRAINT `FK_8` FOREIGN KEY `FK_3` (`id_cartao`) REFERENCES `tb_cartao` (`id_cartao`)
);

CREATE TABLE `tb_categoria`
(
 `id_categoria` int NOT NULL AUTO_INCREMENT ,
 `nm_categoria` varchar(50) NOT NULL ,

PRIMARY KEY (`id_categoria`),
UNIQUE KEY `uk_nm_categoria` (`nm_categoria`)
);

CREATE TABLE `tb_produto`
(
 `id_produto`   int NOT NULL AUTO_INCREMENT ,
 `nm_produto`   varchar(50) NOT NULL ,
 `cd_usuario`   int NULL ,
 `cd_categoria` int NOT NULL ,
 `img_produto`  text NOT NULL ,
 `desc_produto` text NOT NULL ,
 `est_produto`  int NOT NULL ,

PRIMARY KEY (`id_produto`),
KEY `FK_2` (`cd_categoria`),
CONSTRAINT `FK_9` FOREIGN KEY `FK_2` (`cd_categoria`) REFERENCES `tb_categoria` (`id_categoria`),
KEY `FK_3` (`cd_usuario`),
CONSTRAINT `FK_15` FOREIGN KEY `FK_3` (`cd_usuario`) REFERENCES `tb_usuario` (`id_usuario`)
);

CREATE TABLE `tb_compra`
(
 `id_compra`           int NOT NULL ,
 `dt_compra`           date NOT NULL ,
 `cd_endereco_usuario` int NOT NULL ,
 `cd_usuario`          int NOT NULL ,
 `cd_cartao_usuario`   int NULL ,
 `vlr_compra`          decimal(10,2) NOT NULL ,

PRIMARY KEY (`id_compra`),
KEY `FK_2` (`cd_usuario`),
CONSTRAINT `FK_10` FOREIGN KEY `FK_2` (`cd_usuario`) REFERENCES `tb_usuario` (`id_usuario`),
KEY `FK_5` (`cd_endereco_usuario`),
CONSTRAINT `FK_13` FOREIGN KEY `FK_5` (`cd_endereco_usuario`) REFERENCES `tb_endereco__usuario` (`id_endereco_usuario`),
KEY `FK_6` (`cd_cartao_usuario`),
CONSTRAINT `FK_14` FOREIGN KEY `FK_6` (`cd_cartao_usuario`) REFERENCES `tb_cartao_usuario` (`id_cartao_usuario`)
);

CREATE TABLE `tb_itens`
(
 `id_prod_compra` int NOT NULL AUTO_INCREMENT ,
 `cd_produto`     int NOT NULL ,
 `cd_compra`      int NOT NULL ,
 `qtd_produto`    int NOT NULL ,

PRIMARY KEY (`id_prod_compra`),
UNIQUE KEY `fk_produto_compra` (`cd_produto`, `cd_compra`),
KEY `FK_2` (`cd_produto`),
CONSTRAINT `FK_15_1` FOREIGN KEY `FK_2` (`cd_produto`) REFERENCES `tb_produto` (`id_produto`),
KEY `FK_3` (`cd_compra`),
CONSTRAINT `FK_16` FOREIGN KEY `FK_3` (`cd_compra`) REFERENCES `tb_compra` (`id_compra`)
);

CREATE TABLE `tb_forma_de_pagamento`
(
 `id_forma_de_pagamento` int NOT NULL AUTO_INCREMENT ,
 `nm_forma_de_pagamento` varchar(15) NOT NULL ,

PRIMARY KEY (`id_forma_de_pagamento`),
UNIQUE KEY `uk_nm_forma_de_pagamento` (`nm_forma_de_pagamento`)
);

CREATE TABLE `tb_confirmacao_pagamento`
(
 `id_confirmacao_pagamento` int NOT NULL AUTO_INCREMENT ,
 `dt_confirmacao_pagamento` datetime NOT NULL ,
 `cd_compra`                int NOT NULL ,
 `cd_forma_de_pagamento`    int NOT NULL ,

PRIMARY KEY (`id_confirmacao_pagamento`),
KEY `FK_2` (`cd_forma_de_pagamento`),
CONSTRAINT `FK_16_1` FOREIGN KEY `FK_2` (`cd_forma_de_pagamento`) REFERENCES `tb_forma_de_pagamento` (`id_forma_de_pagamento`),
KEY `FK_3` (`cd_compra`),
CONSTRAINT `FK_17` FOREIGN KEY `FK_3` (`cd_compra`) REFERENCES `tb_compra` (`id_compra`)
);