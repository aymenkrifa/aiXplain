__author__ = "aiXplain"

"""
Copyright 2022 The aiXplain SDK authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author: Michael Lam
Date: September 18th 2023
Description:
    Model Factory CLI
"""

from aixplain.factories.model_factory import ModelFactory
from typing import Dict, List, Optional, Text
import click

@click.command("hosts")
@click.option("--api-key", default=None)
def list_host_machines(api_key: Optional[Text] = None) -> None:
    """CLI wrapper function for the LIST_HOST_MACHINES function in 
    ModelFactory.

    Args:
        api_key (Text, optional): Team API key. Defaults to None.

    Returns:
        None
    """
    ret_val = ModelFactory.list_host_machines(api_key)
    click.echo(ret_val)

@click.command("functions")
@click.option("--verbose", default=False)
@click.option("--api-key", default=None)
def list_functions(verbose: bool, api_key: Optional[Text] = None) -> None:
    """CLI wrapper function for the LIST_FUNCTIONS function in ModelFactory.

    Args:
        verbose (Boolean, optional): Set to True if a detailed response 
            is desired; is otherwise False by default.
        api_key (Text, optional): Team API key. Defaults to None.
    Returns:
        None
    """
    ret_val = ModelFactory.list_functions(verbose, api_key)
    click.echo(ret_val)

@click.command("image-repo")
@click.option("--name")
@click.option("--hosting-machine")
@click.option("--version")
@click.option("--description")
@click.option("--function")
@click.option("--source-language", default="en")
@click.option("--api-key", default=None)
def create_asset_repo(name: Text, hosting_machine: Text, version: Text, 
                          description: Text, function: Text, 
                          source_language: Text, 
                          api_key: Optional[Text] = None) -> None:
    """CLI wrapper function for the CREATE_ASSET_REPO function in ModelFactory.

    Args:
        name (Text): Model name
        hosting_machine (Text): Hosting machine ID obtained via list_host_machines
        always_on (bool): Whether the model should always be on
        version (Text): Model version
        description (Text): Model description
        function (Text): Model function name obtained via LIST_HOST_MACHINES
        is_async (bool): Whether the model is asynchronous or not (False in first release)
        source_language (Text): 2-character 639-1 code or 3-character 639-3 language code.
        api_key (Text, optional): Team API key. Defaults to None.

    Returns:
        None
    """
    ret_val = ModelFactory.create_asset_repo(name, hosting_machine, version, 
                                             description, function, 
                                             source_language, api_key)
    click.echo(ret_val)

@click.command("image-repo-login")
@click.option("--api-key", default=None)
def asset_repo_login(api_key: Optional[Text] = None) -> None:
    """CLI wrapper function for the ASSET_REPO_LOGIN function in ModelFactory.

    Args:
        api_key (Text, optional): Team API key. Defaults to None.

    Returns:
        None
    """
    ret_val = ModelFactory.asset_repo_login(api_key)
    click.echo(ret_val)

@click.command("model")
@click.option("--model-id")
@click.option("--image-tag")
@click.option("--image-hash")
@click.option("--api-key", default=None)
def onboard_model(model_id: Text, image_tag: Text, image_hash: Text, 
                  api_key: Optional[Text] = None) -> None:
    """CLI wrapper function for the ONBOARD_MODEL function in ModelFactory.

    Args:
        model_id (Text): Model ID obtained from CREATE_ASSET_REPO.
        image_tag (Text): Image tag to be onboarded.
        api_key (Text, optional): Team API key. Defaults to None.

    Returns:
        None
    """   
    ret_val = ModelFactory.onboard_model(model_id, image_tag, image_hash, api_key)
    click.echo(ret_val)