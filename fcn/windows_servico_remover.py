# Remover serviços rodando em Serviços

    - Abra serviços no windows de 2 cliks no serviço que queira apagar
      copie o sei nome em: "nome do serviço" 

    - Abro o cmd como administrador

        $ sc delete "nome do serviço"
        [SC] DeleteService ÊXITO 

        

# Removendo um serviço via powerSell dos servocoes desnecessarios do windows

    $ powershell “Get-AppxPackage *BingNews* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *BingSports* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *BingWeather* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *Getstarted* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *MicrosoftOfficeHub* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *MicrosoftSolitaireCollection* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *Office.OneNote* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *People* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *SkypeApp* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *Windows.Photos* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *WindowsAlarms* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *WindowsCalculator* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *WindowsCamera* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *WindowsMaps* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *WindowsPhone* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *WindowsSoundRecorder* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *XboxApp* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *ZuneMusic* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *ZuneVideo* | Remove-AppxPackage”
    $ powershell “Get-AppxPackage *3DBuilder* | Remove-AppxPackage