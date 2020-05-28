
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.internal.MouseAction.Button;

public class Pesquisa {
	
	FirefoxDriver navegador;
	
	@Before
	public void antes() {
		System.setProperty("webdriver.gecko.driver", "C:\\Eclipse\\geckodriver\\geckodriver.exe");
		navegador = new FirefoxDriver();
		navegador.get("https://www.senacrs.com.br/");
		navegador.manage().window().maximize();
	}
	
	@Test
	public void test() {
		
		WebElement campo = navegador.findElementByName("busca");
		campo.sendKeys("ads");
		
		WebElement botao = navegador.findElementByXPath("//*[@id=\"cabecalho\"]/div[1]/form/div/img");
		botao.click();
		
		
	}
	
	@After
	public void depois() {
		
	}

}
