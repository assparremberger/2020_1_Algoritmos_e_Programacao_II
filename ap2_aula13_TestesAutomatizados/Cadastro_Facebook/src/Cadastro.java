import java.util.List;

import javax.swing.JOptionPane;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class Cadastro {
	
	FirefoxDriver navegador;
	
	@Before
	public void before() {
		System.setProperty("webdriver.gecko.driver", "C:\\Eclipse\\geckodriver\\geckodriver.exe");
		navegador = new FirefoxDriver();
		navegador.get("https://www.facebook.com/r.php?locale=pt_BR");
		navegador.manage().window().maximize();
	}

	@Test
	public void test() {
		WebElement nome = navegador.findElementByName("firstname");
		WebElement sobrenome = navegador.findElementByName("lastname");
		WebElement email = navegador.findElementByName("reg_email__");
		WebElement senha = navegador.findElementByName("reg_passwd__");
		nome.sendKeys("Maria");
		sobrenome.sendKeys("da silva");
		email.sendKeys("maria@maria.com");
		senha.sendKeys("123abc@@");
		
		Select dia = new Select( navegador.findElementById("day") ) ;
		dia.selectByIndex(5);
		Select mes = new Select( navegador.findElementById("month") ) ;
		mes.selectByValue("2");
		Select ano = new Select( navegador.findElementById("year") ) ;
		ano.selectByVisibleText("1986");
		
		List<WebElement> sexo = navegador.findElementsByName("sex");
		for (WebElement webElement : sexo) {
			if( webElement.getAttribute("value").equals("1") ){
				webElement.click();
			}
		}
		
		WebElement confEmail = navegador.findElementByName("reg_email_confirmation__");
		confEmail.sendKeys("maria@maria.com");
		
		WebElement botao = navegador.findElementByName("websubmit");
		botao.click();
		

		
		
	}
	
	@After
	public void after() {
		try {
			WebElement label = navegador.findElementByXPath("/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div[2]/div/span");
			if( label.getText().equals("maria@maria.com") ) {
				JOptionPane.showMessageDialog(null,"Teste OK");
			}else {
				JOptionPane.showMessageDialog(null,"Erro Teste");
			}
		}catch (Exception e) {
			// TODO: handle exception
			JOptionPane.showMessageDialog(null,"Erro no Teste");
		}
	}

}
