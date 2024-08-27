def fecharAbas(driver,By):
    janelas = driver.find_elements(By.CLASS_NAME,"msg-convo-wrapper")
    if len(janelas) > 0 :
        for i in janelas:
            try:
                botoes = driver.find_elements(By.TAG_NAME,"button")
                for n in botoes:
                    if "Fechar conversa com" in n.text:
                        n.click()
            except:
                continue
            
            
def acessar_perfil(driver,webdriver,By,Keys,time,random):
    contador = 0
    janelas_abertas = driver.window_handles     
    driver.switch_to.window(janelas_abertas[1])
    while True:
        time.sleep(2)
        fecharAbas(driver,By)
        cards = driver.find_elements(By.CLASS_NAME,"reusable-search__result-container")
        links = list(map(lambda x : x.find_element(By.CSS_SELECTOR, 'li.reusable-search__result-container a.app-aware-link').get_attribute('href'),cards))
        textos = list(map(lambda x : x.text, cards))
        time.sleep(2)
        for i in range(len(links)):
            driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)
            if "Pendente" not in textos[i]:
                fecharAbas(driver,By)
                driver.switch_to.window(janelas_abertas[1])
                time.sleep(1)
                driver.get(links[i])
                time.sleep(random.randint(2, 4))
                fecharAbas(driver,By)
                nome = driver.find_element(By.TAG_NAME,"h1").text.split()[0]
                teste3 = True
                if teste3:
                    time.sleep(random.randint(2, 4))
                    fecharAbas(driver,By)    
                    print(str(contador)+" - "+nome)
                    contador += 1
            
        driver.switch_to.window(janelas_abertas[0])
        time.sleep(1)        
        botoes = driver.find_elements(By.CLASS_NAME,"artdeco-button__text")
        for i in botoes:
            if i.text == "Avançar":
                fecharAbas(driver,By)
                i.click()
                time.sleep(random.randint(2, 8))
                
                
def acessar_e_adicionar(driver,webdriver,By,Keys,time,random):
    contador = 0
    janelas_abertas = driver.window_handles  
    driver.switch_to.window(janelas_abertas[1])
    while True:
        time.sleep(2)
        fecharAbas(driver,By)
        cards = driver.find_elements(By.CLASS_NAME,"reusable-search__result-container")
        links = list(map(lambda x : x.find_element(By.CSS_SELECTOR, 'li.reusable-search__result-container a.app-aware-link').get_attribute('href'),cards))
        textos = list(map(lambda x : x.text, cards))
        time.sleep(2)
        for i in range(len(links)):
            if "Pendente" not in textos[i]:
                driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN)
                fecharAbas(driver,By)
                driver.switch_to.window(janelas_abertas[1])
                time.sleep(1)
                driver.get(links[i])
                time.sleep(random.randint(2, 4))
                fecharAbas(driver,By)
                nome = driver.find_element(By.TAG_NAME,"h1").text.split()[0]

                teste = True
                teste2 = True
                teste3 = False
                cabecalho = driver.find_element(By.CLASS_NAME,"ph5")
                botoes_conectar = cabecalho.find_elements(By.TAG_NAME,"button")
                for i in botoes_conectar:
                    if i.text == "Conectar":
                        time.sleep(random.randint(2, 4))
                        fecharAbas(driver,By)
                        i.click()
                        teste3 = True
                        teste = False
                    if i.text == "Pendente":
                        teste2 = False 
                if teste3:
                    time.sleep(random.randint(2, 4))                          
                    modal = driver.find_element(By.CLASS_NAME,"artdeco-modal")
                    button = modal.find_elements(By.TAG_NAME,"button")
                    fecharAbas(driver,By)
                    button[1].click()
                    time.sleep(random.randint(2, 20))
                    fecharAbas(driver,By)
                    frase = "Oi, %s! Como vai?\n\nGostaria de me conectar com você. Estou em busca da minha primeira vaga como Dev Back-end Junior. Estudo ADS na FIAP, inglês, estou me especializando em Java + Spring e possuo 5 anos como analista de dados.\n\nE agradeço por dicas e oportunidades.\n\nAbraços!!!"%nome  
                    fecharAbas(driver,By)
                    driver.find_element(By.ID,"custom-message").send_keys(frase)
                    time.sleep(random.randint(2, 15))
                    modal = driver.find_element(By.CLASS_NAME,"artdeco-modal")
                    button = modal.find_elements(By.TAG_NAME,"button")
                    fecharAbas(driver,By)
                    button[2].click()
                    time.sleep(random.randint(2, 4))     
                    print(str(contador)+" - "+nome)
                    contador += 1

        driver.switch_to.window(janelas_abertas[0])
        time.sleep(1)        
        botoes = driver.find_elements(By.CLASS_NAME,"artdeco-button__text")
        for i in botoes:
            if i.text == "Avançar":
                fecharAbas(driver,By)
                i.click()
                time.sleep(random.randint(2, 8))