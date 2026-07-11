<?php


if(isset($_GET['specific_role'])):


	$role_id = isset($_GET['role_id']) ? $fieldValidator->validate_field($_GET['role_id']) : "";

	$workspacerolemap_array = array();
	$role_array = array();
	$workspace_array = array();

	$query = $queryExecutor->execute($selectionObj->select_role($role_id));

	while($row = mysqli_fetch_array($query)):

		$role_id = $row['role_id'];
		$role_array[$role_id] = array();
		$role_array[$role_id]['role_id'] = $role_id;

		$key = $role_id;

		$dependent_query = $queryExecutor->execute($selectionObj->select_role_name($role_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$role_array[$key]['name'] = $row_col['name'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_role_description($role_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$role_array[$key]['description'] = $row_col['description'];


		$secondary_query = $queryExecutor->execute($selectionObj->select_workspacerolemap_by_role($role_id));

		while($sec_row = mysqli_fetch_array($secondary_query)):

			$workspace_id = $sec_row['workspace_id'];
			$workspace_array[$workspace_id] = array();
			$workspace_array[$workspace_id]['workspace_id'] = $workspace_id;

			$sec_key = $workspace_id;

			$dependent_query = $queryExecutor->execute($selectionObj->select_workspace_name($workspace_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workspace_array[$sec_key]['name'] = $row_col['name'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_workspace_description($workspace_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workspace_array[$sec_key]['description'] = $row_col['description'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_workspace_email($workspace_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workspace_array[$sec_key]['email'] = $row_col['email'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_workspace_country($workspace_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workspace_array[$sec_key]['country'] = $row_col['country'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_workspace_language($workspace_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workspace_array[$sec_key]['language'] = $row_col['language'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_workspace_organization_type($workspace_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$workspace_array[$sec_key]['organization_type'] = $row_col['organization_type'];

		endwhile;



	endwhile;


?>

<table cellspacing = "1" cellpadding = "0" align = "center" width = "100%" id = "workspacerolemap">
 <tr>
 <td colspan = "7">&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td colspan = "2"><a href="target_print.php?workspacerolemap&&role_id=<?= $role_id ?>" target="_blank" style="color:#00FF00;">Print PDF</a></td></tr>
 <tr class = "top_row">
 <td>&nbsp;&nbsp;#&nbsp;&nbsp;</td>
 <td>&nbsp;Workspace id&nbsp;</td>
 <td>&nbsp;Name&nbsp;</td>
 <td>&nbsp;Description&nbsp;</td>
 <td>&nbsp;Email&nbsp;</td>
 <td>&nbsp;Country&nbsp;</td>
 <td>&nbsp;Language&nbsp;</td>
 <td>&nbsp;Organization type&nbsp;</td>
 <td>&nbsp;&nbsp;Actions&nbsp;&nbsp;</td></tr>
 
<?php $i = 0; ?>


<?php  foreach($workspace_array as $workspace_key => $workspace_value): ?>
<?php $css_class = ($i+1)%2 == 0 ? "even_row" : "odd_row"; ?>


<tr>
	<td><?= ($i+1) ?></td>
	<td><?= $workspace_value['workspace_id'] ?></td>
	<td><?= $workspace_value['name'] ?></td>
	<td><?= $workspace_value['description'] ?></td>
	<td><?= $workspace_value['email'] ?></td>
	<td><?= $workspace_value['country'] ?></td>
	<td><?= $workspace_value['language'] ?></td>
	<td><?= $workspace_value['organization_type'] ?></td>
	<td>

		<?php $id_string = $workspace_id; ?>

		<div id="update_workspace_<?= $id_string ?>" style="display:none" class="updates">
		<table border="0" align="center" class="overlay_contained_table">
		<tr>
			<td align="right">
			<div class="closebtn" id="close_circle" onclick="closeUpdateOverlay('update_workspace_<?= $id_string ?>');">&nbsp;&times;&nbsp;</div>
			</td>
		</tr>
		<tr><td><br /></td></tr>
		<tr>
			<td align="center">
			<fieldset style="width: 80%">
			<legend>workspace Information</legend>
			<?php update_workspace($queryExecutor, $selectionObj, $updateObj, $fieldValidator, $workspace_value['workspace_id']); ?>
			</fieldset>
			</td>
		</tr>
		<tr>
			<td><br /></td>
		</tr>
		</table>
		</div>


<?php

	$workspacerolemap_count = count_workspacerolemap($queryExecutor, $selectionObj);
	$mapping_link = "workspacerolemap.php?workspace&&workspace_id=".$workspace_value['workspace_id']."";
	$title = "workspacerolemap corresponding entries.";
	$label = "Wor.";
	get_mapping_mark_up($workspacerolemap_count, $mapping_link, $title, $label);



?>


	<label id="update_link_<?= $id_string ?>" onclick="showUpdate('update_<?= $id_string ?>');" style="cursor:pointer">
	<img src="images/icons/edit.png" width="15px" height="15px" title="edit entry" style="cursor:pointer" />
	</label> 
 &nbsp; 
	<?php 
		$link = "workspace.php?delete_Workspace&&workspace_id=".$workspace_value['workspace_id']."";
		$message = "";
	?>

	<?php showConfirmDeleteAction($id_string, $link, $message); ?>
	<label style="cursor:pointer" onclick="showDelete('delete_<?= $id_string ?>')">
	<img src="images/icons/delete.png" width="15px" height="15px" title="delete entry" />
	</label>
	</td>
<tr>
	<?php $i = ($i + 1); ?>
<?php endforeach; ?>
 <tr>
 <td colspan = "9"></td></tr></table>

<?php endif; ?>

