from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure import pages
import csv


template = """
???+ comments "*{score}* | {name}"
{content}
""".strip()

expert_url = "![](https://img.shields.io/badge/-Expert-blue?style=flat-square&color=rgb(127%2C%20161%2C%20195))"

class CommentsPlugin(BasePlugin):
    config_scheme = (
        ("enabled",config_options.Type(bool,default=True)),
        ("folded",config_options.Type(bool,default=False)),
        ("csv_data",config_options.Type(list,default=[]))
    )


    def on_config(self,config:config_options.Config):
        if not self.config.get("enabled"):
            return config
        
        csv_data = self.config.get("csv_data")
        plugin_data = list()
        for csv_file in csv_data:
            with open(csv_file, "r", encoding="UTF-8") as f:
                cdata = list(csv.DictReader(f))
                for row in cdata:
                    row["source"] = csv_file
                plugin_data.extend(cdata)
        self.data = plugin_data
        return config


    def on_page_markdown(self,markdown,page:pages.Page,config: config_options.Config,files,**kwargs):
        if not self.config.get("enabled"):
            return markdown
        # if not page.meta.get("comments"):
        #     return markdown
        if "{{comments}}" not in markdown:
            return markdown
        markdown = markdown.replace(
            "{{comments}}",
            self._get_page_markdown(markdown[markdown.find("{{source=")+9:markdown.rfind("}}")])
        )
        markdown = markdown[:markdown.find("{{source="):]
        return markdown

    def _get_page_markdown(self, source)->str:
        markdown= ""
        pos_list = list(set(list(map(lambda x: x['位置'], filter(lambda x: x['source'] == source, self.data)))))
        print(source, pos_list)
        for pos in pos_list:
            markdown+=f"## {pos}\n\n"
            shops = list(filter(lambda x:x['位置']==pos,self.data))
            shops_list = list(set(list(map(lambda x: x['名称'],shops))))
            for shop in shops_list:
                markdown+=f"### {shop} \n\n"
                names = list(filter(lambda x:x['名称']==shop,shops))
                names_list = list(set(list(map(lambda x: x['名称'],names))))
                for name in names:
                    markdown+=template.format(
                        score = name['定位'],
                        name = name['姓名']+(expert_url if name['专家']=='True' else ''),
                        content = self._indent(name['评价'])
                    )+'\n'
                markdown+='\n'
            markdown+='\n'
        # print(markdown)
        return markdown
    
    @staticmethod
    def _indent(text:str,amount=4):
        return "\n".join(" "*amount + line for line in text.splitlines())
