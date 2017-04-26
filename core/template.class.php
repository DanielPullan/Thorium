<?php
	namespace Krypton;

	class Template
	{
		private $assignedValues = array();
		private $partialBuffer;
		private $tpl;
		//Construct Function (First steps, checks if exists)
		function __construct($_path = '')
		{
			if(!empty($_path))
			{
				if(file_exists($_path))
				{
					ob_start();
					include($_path);
					$this->tpl .= ob_get_contents();
					ob_end_clean();
				}
				else
				{
					echo "Krypton Template System Error: File not found! PATH = ".$_path;
				}
			}

		}
		//The assigned Parameters {url} etc.
		function SetParams()
		{
			global $_CONFIG;
			$this->Assign('url', $_CONFIG['site']['url']); //{URL} Site URL
			$this->Assign('tpl', $_CONFIG['site']['template']); //{TPL} Skin Name
			$this->Assign('site_name', $_CONFIG['site']['name']); //{SITE_NAME} Site Name
			$this->Assign('tw', $_CONFIG['site']['tw']); //{TW} Twitter
			$this->Assign('fb', $_CONFIG['site']['fb']); //{FB} Facebook
			$this->Assign('twapi', $_CONFIG['site']['twapi']); //{tawpi} Twitter API
			$this->Assign('banner', $_CONFIG['site']['banner']); //{banner} Banner if one exists

		}
		//This function takes the set params and turns them into an actual function
		function Assign($_searchString, $_replaceString)
		{
			if(!empty($_searchString))
			{
				$this->assignedValues[strtoupper($_searchString)] = $_replaceString;
			}
		}
		//Add Template Pieces (Basically import raw PHP // I'm confident there is a bettter way but for now #YOLO)

		//Combines everything and echo's the template
		function Show()
		{
			if(count($this->assignedValues) > 0)
			{
				foreach ($this->assignedValues as $key => $value)
				{
					$this->tpl = str_ireplace('{'.$key.'}', $value, $this->tpl);
				}
			}
			echo $this->tpl;
		}
	}

?>
